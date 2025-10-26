CREATE VIEW dataset AS
SELECT
    c.ageGroup,
    p.gender,
    -- prescription: any disease except astigmatic
    MAX(d.diseaseName) FILTER (WHERE d.diseaseName <> 'astigmatic') AS prescription,
    -- astigmatic: yes/no
    CASE WHEN COUNT(*) FILTER (WHERE d.diseaseName = 'astigmatic') > 0 THEN 'yes' ELSE 'no' END AS astigmatic,
    c.tearRate,
    c.lenses
FROM CONSULTATION c
JOIN PATIENT p ON c.patientId = p.patientId
JOIN DIAGNOSIS dg ON c.consultationId = dg.consultationId
JOIN DISEASE d ON dg.diseaseId = d.diseaseId
GROUP BY c.consultationId, c.ageGroup, p.gender, c.tearRate, c.lenses
ORDER BY c.ageGroup DESC;


CREATE VIEW dataset_3row AS
SELECT * FROM (
    -- Second row: types
    SELECT 'd' AS ageGroup, 'd' AS gender, 'd' AS prescription,
           'd' AS astigmatic, 'd' AS tearRate, 'd' AS lenses
    UNION ALL
    -- Third row: roles
    SELECT NULL,NULL,NULL,NULL,NULL,'class'
    UNION ALL
    -- Actual data
    SELECT ageGroup, gender, prescription, astigmatic, tearRate, lenses
    FROM dataset
) t;
