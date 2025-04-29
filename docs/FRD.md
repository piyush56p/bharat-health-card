# Functional Requirements Document (FRD)

## Project Name: Bharat Health Card

### Objective
To create a unified digital health identity system for Indian citizens, accessible from any hospital or clinic in the country.

---

## Modules

### 1. Patient Management
- Register patient with personal and location info (State, District, Aadhaar optional)
- View patient profile
- Link all records to patient ID

### 2. Doctor Management
- Register doctors with MCI/NMC number
- Login functionality
- Add/view medical records for a patient

### 3. Medical Records
- Create a new record: diagnosis, prescription, notes
- View records history by date
- Store hospital name and department info

---

## Data Fields (Core)

### Patient
- Full Name
- Gender
- DOB
- Aadhaar Number (optional)
- State, District, Pincode
- Blood Group
- Language Preference

### Doctor
- Name
- MCI/NMC Registration Number
- Hospital/Clinic Name
- Specialization

### Medical Record
- Visit Date
- Record Type (Consultation, Emergency, etc.)
- Diagnosis Notes
- Prescribed Medications
- Upload Scanned Report (optional)

---

## Future Enhancements
- Multi-language support
- Mobile OTP login
- Government hospital API sync
