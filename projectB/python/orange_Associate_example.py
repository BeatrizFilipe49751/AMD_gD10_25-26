#_______________________________________________________________________________
# Modules to Evaluate
import sys
import Orange
from orangecontrib.associate.fpgrowth import *

#_______________________________________________________________________________
# Question 7 – Controlled exploration of support/confidence
#_______________________________________________________________________________

# Calculates association rules given the support and confidence ranges
def explore_rules(supports, confidences, X, maxR):
    results = []

    for support in supports:
        print(f"Trying support={support}")
        # Get frequent itemsets based on the current support
        setOf_itemset = frequent_itemsets( X, support )
        # Convert the set of itemsets to a dictionary
        dict_setOf_itemset = dict( setOf_itemset )

        print(f"  Found {len(dict_setOf_itemset)} itemsets")

        if not dict_setOf_itemset:
            continue

        for confidence in confidences:
            rules = []
            exceeded = False
            # Use generator to avoid building the full list at once
            for rule in association_rules(dict_setOf_itemset, confidence):
                rules.append(rule)
                if len(rules) >= maxR:
                    # Stop early if reached maxR rules
                    exceeded = True
                    break
            
            if not exceeded and rules: # accept only if <= maxR
                results.append((support, confidence, dict_setOf_itemset, rules))
                print(f"  Support={support}, Confidence={confidence} → {len(rules)} rules")
            
            # Generate association rules from the frequent itemsets with the current confidence
            #setOf_rule = association_rules( dict_setOf_itemset, confidence )
            #list_setOf_rule = list( setOf_rule )
            #print(f"    confidence={confidence} → {len(list_setOf_rule)} rules")

            #if 0 < len(list_setOf_rule) <= maxR:
            #    results.append((support, confidence, dict_setOf_itemset, list_setOf_rule))

    return results


#_______________________________________________________________________________
# decode the itemsets back to their original values
def decode_itemsets(dict_setOf_itemset, Xbasket, mapping):
    decoded_itemsets = []
    for itemset in dict_setOf_itemset.keys():
        supp = dict_setOf_itemset[itemset]
        decoded_itemset = [ var.name for _, var, _ in OneHot.decode( itemset, Xbasket, mapping ) ]
        tuple_itemset = ( decoded_itemset, supp )
        decoded_itemsets.append( tuple_itemset )
    return decoded_itemsets


#_______________________________________________________________________________
# decode the setOf-rules back to their original values
def decode_rules(list_setOf_rule, Xbasket, mapping):
    decoded_rules = []
    for rule in list_setOf_rule:
        LHS, RHS, supp, conf = rule
        decoded_LHS = [ var.name for _, var, _ in OneHot.decode( LHS, Xbasket, mapping ) ]
        decoded_RHS = [ var.name for _, var, _ in OneHot.decode( RHS, Xbasket, mapping ) ]
        tuple_rule = ( decoded_LHS, decoded_RHS, supp, conf )
        decoded_rules.append( tuple_rule )
    return decoded_rules


# _______________________________________________________________________________
# Main code
if __name__ == "__main__":
    # read the dataset (basket format)
    Xbasket = Orange.data.Table( "../docs/zz_dataset_2012_01.basket" )
    
    # make the OneHot transform in order to apply the "associate" methods
    X, mapping = OneHot.encode( Xbasket )
    
    # Maximum number of rules to be generated
    if len(sys.argv) != 2:
        maxR = 20
    else:
        maxR = int(sys.argv[1])
    print(f"Maximum number of rules allowed: {maxR}")
    
    # The support and confidence ranges to explore
    supports = [3]  # Example: supports 2, 3, and 4
    confidences = [0.95, 0.9, 0.8]  # Example: confidences 60%, 70%, 90%, and 95%

    results = explore_rules(supports, confidences, X, maxR)
    
    for support, confidence, itemsets, rules in results:
        print(f"\nSupport={support}, Confidence={confidence}")

        decoded_itemsets = decode_itemsets(itemsets, Xbasket, mapping)
        decoded_rules = decode_rules(rules, Xbasket, mapping)

        print("Frequent itemsets:")
        for it in decoded_itemsets:
            print(it)

        print("Rules:")
        for r in decoded_rules:
            print(r)