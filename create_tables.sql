-- 1. DOCTOR
CREATE TABLE DOCTOR (
    doctorId SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100),
    phoneNumber VARCHAR(20)
);

-- 2. PATIENT
CREATE TABLE PATIENT (
    patientId SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    birthDate DATE NOT NULL,
    gender CHAR(1) CHECK (gender IN ('M', 'F')),
    phoneNumber VARCHAR(20)
);

-- 3. DISEASE
CREATE TABLE DISEASE (
    diseaseId SERIAL PRIMARY KEY,
    diseaseName VARCHAR(50) UNIQUE NOT NULL
);

-- 4. CONSULTATION
CREATE TABLE CONSULTATION (
    consultationId SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    ageGroup VARCHAR(20) CHECK (ageGroup IN ('young', 'pre-presbyopic', 'presbyopic')),
    tearRate VARCHAR(10) CHECK (tearRate IN ('normal', 'reduced')),
    lenses VARCHAR(10) CHECK (lenses IN ('none', 'soft', 'hard')),
    patientId INT REFERENCES PATIENT(patientId) ON DELETE CASCADE,
    doctorId INT REFERENCES DOCTOR(doctorId) ON DELETE CASCADE
);

-- 5. DIAGNOSIS (associative table CONSULTATION-DISEASE)
CREATE TABLE DIAGNOSIS (
    consultationId INT REFERENCES CONSULTATION(consultationId) ON DELETE CASCADE,
    diseaseId INT REFERENCES DISEASE(diseaseId) ON DELETE CASCADE,
    notes TEXT,
    PRIMARY KEY (consultationId, diseaseId)
);


-- This trigger runs BEFORE INSERT or UPDATE on the CONSULTATION table.
-- It calculates the patient's age at the time of the consultation (based on birthDate)
-- and assigns the ageGroup:
--   - 'young' for age < 30
--   - 'pre-presbyopic' for age 30–39
--   - 'presbyopic' for age >= 40
CREATE OR REPLACE FUNCTION set_age_group()
RETURNS TRIGGER AS $$
BEGIN
    NEW.ageGroup := CASE 
        WHEN DATE_PART('year', AGE(NEW.date, (SELECT birthDate FROM PATIENT WHERE patientId = NEW.patientId))) < 30 THEN 'young'
        WHEN DATE_PART('year', AGE(NEW.date, (SELECT birthDate FROM PATIENT WHERE patientId = NEW.patientId))) BETWEEN 30 AND 39 THEN 'pre-presbyopic'
        ELSE 'presbyopic'
    END;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_set_age_group
BEFORE INSERT OR UPDATE ON CONSULTATION
FOR EACH ROW
EXECUTE FUNCTION set_age_group();
