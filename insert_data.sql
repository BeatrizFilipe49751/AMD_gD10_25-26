-- 1. DOCTOR
INSERT INTO DOCTOR (name, specialization, phoneNumber) VALUES
('Dr. Alice Smith', 'Cornea', '+1-555-0101'),
('Dr. Bob Johnson', 'Retina', '+1-555-0102'),
('Dr. Emily Carter', 'General Ophthalmology', '+1-555-0103');

-- 2. PATIENT
INSERT INTO PATIENT (name, birthDate, gender, phoneNumber) VALUES
('John Doe', '2000-04-10', 'M', '+1-555-1001'),
('Mary Jane', '2001-07-22', 'F', '+1-555-1002'),
('Lucas Brown', '1998-02-18', 'M', '+1-555-1003'),
('Emily Davis', '1999-09-05', 'F', '+1-555-1004'),
('Kevin Wilson', '1997-11-12', 'M', '+1-555-1005'),
('Sara White', '1978-02-28', 'F', '+1-555-1006'),
('Alice Green', '1975-11-10', 'F', '+1-555-1007'),
('James Hall', '1969-04-07', 'M', '+1-555-1008'),
('Olivia Turner', '1973-01-15', 'F', '+1-555-1009'),
('Ethan Clark', '1980-06-23', 'M', '+1-555-1010'),
('Sophie Lewis', '1965-08-08', 'F', '+1-555-1011'),
('Michael Scott', '1990-03-15', 'M', '+1-555-1012'),
('Laura King', '1988-09-30', 'F', '+1-555-1013'),
('Daniel Adams', '1993-06-02', 'M', '+1-555-1014'),
('Patricia Young', '1991-12-25', 'F', '+1-555-1015'),
('George Harris', '1989-05-19', 'M', '+1-555-1016');

-- 3. DISEASE
INSERT INTO DISEASE (diseaseName) VALUES
('myope'),
('hypermetrope'),
('astigmatic');

-- 4. CONSULTATION
INSERT INTO CONSULTATION (date, tearRate, lenses, patientId, doctorId) VALUES
('2025-10-01', 'normal', 'hard', 1, 1),  -- young, myope, yes
('2025-10-02', 'normal', 'soft', 2, 2),  -- young, myope, no
('2025-10-03', 'reduced', 'none', 3, 3), -- young, hypermetrope, yes
('2025-10-04', 'normal', 'soft', 4, 1),  -- young, hypermetrope, no
('2025-10-05', 'reduced', 'none', 5, 2), -- young, hypermetrope, no
('2025-10-06', 'reduced', 'none', 6, 3), -- presbyopic, myope, yes
('2025-10-07', 'normal', 'hard', 7, 1),  -- presbyopic, myope, yes
('2025-10-08', 'reduced', 'none', 8, 2), -- presbyopic, hypermetrope, yes
('2025-10-09', 'normal', 'none', 9, 3),  -- presbyopic, hypermetrope, yes
('2025-10-10', 'normal', 'soft', 10, 1),  -- presbyopic, hypermetrope, no
('2025-10-11', 'reduced', 'none', 11, 2), -- presbyopic, hypermetrope, no
('2025-10-12', 'reduced', 'none', 12, 3), -- pre-presbyopic, myope, yes
('2025-10-13', 'normal', 'hard', 13, 1),  -- pre-presbyopic, myope, yes
('2025-10-14', 'normal', 'soft', 14, 2),  -- pre-presbyopic, myope, no
('2025-10-15', 'normal', 'none', 15, 3),  -- pre-presbyopic, hypermetrope, yes
('2025-10-16', 'normal', 'soft', 16, 1);  -- pre-presbyopic, hypermetrope, no

-- 5. DIAGNOSIS (associative table CONSULTATION-DISEASE)
INSERT INTO DIAGNOSIS (consultationId, diseaseId, notes) VALUES
(1, 1, 'myope'),
(1, 3, 'astigmatic'),
(2, 1, 'myope'),
(3, 2, 'hypermetrope'),
(3, 3, 'astigmatic'),
(4, 2, 'hypermetrope'),
(5, 2, 'hypermetrope'),
(6, 1, 'myope'),
(6, 3, 'astigmatic'),
(7, 1, 'myope'),
(7, 3, 'astigmatic'),
(8, 2, 'hypermetrope'),
(8, 3, 'astigmatic'),
(9, 2, 'hypermetrope'),
(9, 3, 'astigmatic'),
(10, 2, 'hypermetrope'),
(11, 2, 'hypermetrope'),
(12, 1, 'myope'),
(12, 3, 'astigmatic'),
(13, 1, 'myope'),
(13, 3, 'astigmatic'),
(14, 1, 'myope'),
(15, 2, 'hypermetrope'),
(15, 3, 'astigmatic'),
(16, 2, 'hypermetrope');