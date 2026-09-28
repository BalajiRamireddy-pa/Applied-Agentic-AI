import streamlit as st 
from datetime import datetime, date 
from pathlib import Path 
import ast 
 
 
# ========================================================= 
# PAGE CONFIGURATION 
# ========================================================= 
 
st.set_page_config( 
    page_title="Hospital Management System", 
    page_icon="🏥", 
    layout="wide" 
) 
 
 
# ========================================================= 
# CUSTOM CSS 
# ========================================================= 
 
st.markdown(""" 
<style> 
 
.main-title { 
    font-size: 40px; 
    font-weight: bold; 
    text-align: center; 
    margin-bottom: 5px; 
} 
 
.subtitle { 
    text-align: center; 
    color: gray; 
    font-size: 18px; 
    margin-bottom: 30px; 
} 
 
.card { 
    padding: 20px; 
    border-radius: 12px; 
    border: 1px solid #ddd; 
    background-color: #ffffff; 
    margin-bottom: 15px; 
} 
 
</style> 
""", unsafe_allow_html=True) 
 
 
# ========================================================= 
# FILE NAMES 
# ========================================================= 
 
PATIENT_FILE = "patients.txt" 
DOCTOR_FILE = "doctors.txt" 
APPOINTMENT_FILE = "appointments.txt" 
 
 
# ========================================================= 
# SESSION STATE 
# ========================================================= 
 
if "patients" not in st.session_state: 
    st.session_state.patients = [] 
 
if "doctors" not in st.session_state: 
    st.session_state.doctors = [] 
 
if "appointments" not in st.session_state: 
    st.session_state.appointments = [] 
 
 
# ========================================================= 
# LOAD DATA FROM FILE 
# ========================================================= 
 
def load_data(filename): 
 
    data = [] 
 
    if Path(filename).exists(): 
 
        try: 
 
            with open(filename, "r", encoding="utf-8") as file: 
 
                for line in file: 
 
                    if line.strip(): 
 
                        data.append(ast.literal_eval(line.strip())) 
 
        except Exception as e: 
 
            st.error(f"Error loading {filename}: {e}") 
 
    return data 
 
 
if not st.session_state.patients: 
    st.session_state.patients = load_data(PATIENT_FILE) 
 
if not st.session_state.doctors: 
    st.session_state.doctors = load_data(DOCTOR_FILE) 
 
if not st.session_state.appointments: 
    st.session_state.appointments = load_data(APPOINTMENT_FILE) 
 
 
# ========================================================= 
# SAVE PATIENTS 
# ========================================================= 
 
def save_patients(): 
 
    try: 
 
        with open(PATIENT_FILE, "w", encoding="utf-8") as file: 
 
            for patient in st.session_state.patients: 
 
                file.write(str(patient) + "\n") 
 
    except Exception as e: 
 
        st.error(f"File Error: {e}") 
 
 
# ========================================================= 
# SAVE DOCTORS 
# ========================================================= 
 
def save_doctors(): 
 
    try: 
 
        with open(DOCTOR_FILE, "w", encoding="utf-8") as file: 
 
            for doctor in st.session_state.doctors: 
 
                file.write(str(doctor) + "\n") 
 
    except Exception as e: 
 
        st.error(f"File Error: {e}") 
 
 
# ========================================================= 
# SAVE APPOINTMENTS 
# ========================================================= 
 
def save_appointments(): 
 
    try: 
 
        with open(APPOINTMENT_FILE, "w", encoding="utf-8") as file: 
 
            for appointment in st.session_state.appointments: 
 
                file.write(str(appointment) + "\n") 
 
    except Exception as e: 
 
        st.error(f"File Error: {e}") 
 
 
# ========================================================= 
# FIND PATIENT 
# ========================================================= 
 
def find_patient(patient_id): 
 
    for patient in st.session_state.patients: 
 
        if patient["id"] == patient_id: 
 
            return patient 
 
    return None 
 
 
# ========================================================= 
# FIND DOCTOR 
# ========================================================= 
 
def find_doctor(doctor_id): 
 
    for doctor in st.session_state.doctors: 
 
        if doctor["id"] == doctor_id: 
 
            return doctor 
 
    return None 
 
 
# ========================================================= 
# HEADER 
# ========================================================= 
 
st.markdown( 
    '<div class="main-title">🏥 Hospital Management System</div>', 
    unsafe_allow_html=True 
) 
 
st.markdown( 
    '<div class="subtitle">Patient • Doctor • Appointment • Billing Management</div>', 
    unsafe_allow_html=True 
) 
 
 
# ========================================================= 
# SIDEBAR 
# ========================================================= 
 
st.sidebar.title("🏥 Hospital System") 
 
menu = st.sidebar.radio( 
    "Select Module", 
    [ 
        "Dashboard", 
        "Patient Registration", 
        "Doctor Registration", 
        "Doctor Allocation", 
        "Appointment Booking", 
        "Appointment Cancellation", 
        "Medical History", 
        "Consultation Charges", 
        "Billing", 
        "Patient Search", 
        "Daily Appointment Report" 
    ] 
) 
 
 
# ========================================================= 
# DASHBOARD 
# ========================================================= 
 
if menu == "Dashboard": 
 
    st.header("📊 Dashboard") 
 
    total_patients = len(st.session_state.patients) 
 
    total_doctors = len(st.session_state.doctors) 
 
    available_doctors = sum( 
        1 
        for doctor in st.session_state.doctors 
        if doctor.get("available", True) 
    ) 
 
    total_appointments = len(st.session_state.appointments) 
 
    col1, col2, col3, col4 = st.columns(4) 
 
    col1.metric( 
        "👤 Total Patients", 
        total_patients 
    ) 
 
    col2.metric( 
        "👨‍⚕️ Total Doctors", 
        total_doctors 
    ) 
 
    col3.metric( 
        "✅ Available Doctors", 
        available_doctors 
    ) 
 
    col4.metric( 
        "📅 Appointments", 
        total_appointments 
    ) 
 
    st.divider() 
 
    st.subheader("👨‍⚕️ Doctor Availability") 
 
    if st.session_state.doctors: 
 
        for doctor in st.session_state.doctors: 
 
            if doctor.get("available", True): 
 
                st.success( 
                    f"🟢 {doctor['name']} - " 
                    f"{doctor['specialization']} - Available" 
                ) 
 
            else: 
 
                st.error( 
                    f"🔴 {doctor['name']} - " 
                    f"{doctor['specialization']} - Allocated" 
                ) 
 
    else: 
 
        st.info("No doctors registered.") 
 
 
# ========================================================= 
# PATIENT REGISTRATION 
# ========================================================= 
 
elif menu == "Patient Registration": 
 
    st.header("👤 Patient Registration") 
 
    with st.form("patient_form"): 
 
        patient_id = st.text_input("Patient ID") 
 
        name = st.text_input("Patient Name") 
 
        age = st.number_input( 
            "Age", 
            min_value=1, 
            max_value=120, 
            step=1 
        ) 
 
        phone = st.text_input("Phone Number") 
 
        submit = st.form_submit_button( 
            "Register Patient" 
        ) 
 
    if submit: 
 
        if not patient_id or not name or not phone: 
 
            st.warning("Please fill all fields.") 
 
        elif find_patient(patient_id): 
 
            st.error("Patient ID already exists!") 
 
        else: 
 
            patient = { 
 
                "id": patient_id, 
 
                "name": name, 
 
                "age": age, 
 
                "phone": phone, 
 
                "doctor": "", 
 
                "history": [] 
            } 
 
            st.session_state.patients.append(patient) 
 
            save_patients() 
 
            st.success( 
                "Patient registered successfully!" 
            ) 
 
 
# ========================================================= 
# DOCTOR REGISTRATION 
# ========================================================= 
 
elif menu == "Doctor Registration": 
 
    st.header("👨‍⚕️ Doctor Registration") 
 
    with st.form("doctor_form"): 
 
        doctor_id = st.text_input("Doctor ID") 
 
        name = st.text_input("Doctor Name") 
 
        age = st.number_input( 
            "Doctor Age", 
            min_value=1, 
            max_value=120, 
            step=1 
        ) 
 
        phone = st.text_input("Phone Number") 
 
        specialization = st.text_input( 
            "Specialization" 
        ) 
 
        charge = st.number_input( 
            "Consultation Charge ₹", 
            min_value=0.0, 
            step=100.0 
        ) 
 
        submit = st.form_submit_button( 
            "Register Doctor" 
        ) 
 
    if submit: 
 
        if not doctor_id or not name or not phone: 
 
            st.warning("Please fill all fields.") 
 
        elif find_doctor(doctor_id): 
 
            st.error("Doctor ID already exists!") 
 
        else: 
 
            doctor = { 
 
                "id": doctor_id, 
 
                "name": name, 
 
                "age": age, 
 
                "phone": phone, 
 
                "specialization": specialization, 
 
                "charge": charge, 
 
                "available": True 
            } 
 
            st.session_state.doctors.append(doctor) 
 
            save_doctors() 
 
            st.success( 
                "Doctor registered successfully!" 
            ) 
 
 
# ========================================================= 
# DOCTOR ALLOCATION 
# ========================================================= 
 
elif menu == "Doctor Allocation": 
 
    st.header("🩺 Doctor Allocation") 
 
    if not st.session_state.patients: 
 
        st.warning("Please register a patient first.") 
 
    elif not st.session_state.doctors: 
 
        st.warning("Please register a doctor first.") 
 
    else: 
 
        patient_ids = [ 
            p["id"] 
            for p in st.session_state.patients 
        ] 
 
        patient_id = st.selectbox( 
            "Select Patient", 
            patient_ids 
        ) 
 
        available_doctors = [ 
 
            d 
            for d in st.session_state.doctors 
            if d.get("available", True) 
 
        ] 
 
        if not available_doctors: 
 
            st.warning( 
                "No doctors are currently available." 
            ) 
 
        else: 
 
            doctor_ids = [ 
                d["id"] 
                for d in available_doctors 
            ] 
 
            doctor_id = st.selectbox( 
                "Select Doctor", 
                doctor_ids 
            ) 
 
            doctor = find_doctor(doctor_id) 
 
            st.info( 
                f"Doctor: {doctor['name']} | " 
                f"Specialization: {doctor['specialization']}" 
            ) 
 
            if st.button( 
                "Allocate Doctor", 
                type="primary" 
            ): 
 
                patient = find_patient(patient_id) 
 
                patient["doctor"] = doctor["name"] 
 
                doctor["available"] = False 
 
                save_patients() 
 
                save_doctors() 
 
                st.success( 
                    f"{doctor['name']} allocated to " 
                    f"{patient['name']}." 
                ) 
 
 
# ========================================================= 
# APPOINTMENT BOOKING 
# ========================================================= 
 
elif menu == "Appointment Booking": 
 
    st.header("📅 Appointment Booking") 
 
    if not st.session_state.patients: 
 
        st.warning("Register a patient first.") 
 
    elif not st.session_state.doctors: 
 
        st.warning("Register a doctor first.") 
 
    else: 
 
        patient_ids = [ 
            p["id"] 
            for p in st.session_state.patients 
        ] 
 
        doctor_ids = [ 
            d["id"] 
            for d in st.session_state.doctors 
        ] 
 
        patient_id = st.selectbox( 
            "Select Patient", 
            patient_ids 
        ) 
 
        doctor_id = st.selectbox( 
            "Select Doctor", 
            doctor_ids 
        ) 
 
        appointment_date = st.date_input( 
            "Appointment Date", 
            min_value=date.today() 
        ) 
 
        appointment_time = st.time_input( 
            "Appointment Time" 
        ) 
 
        if st.button( 
            "Book Appointment", 
            type="primary" 
        ): 
 
            date_text = appointment_date.strftime( 
                "%d-%m-%Y" 
            ) 
 
            time_text = appointment_time.strftime( 
                "%H:%M" 
            ) 
 
            appointment = { 
 
                "patient_id": patient_id, 
 
                "doctor_id": doctor_id, 
 
                "date": date_text, 
 
                "time": time_text, 
 
                "status": "Booked" 
            } 
 
            st.session_state.appointments.append( 
                appointment 
            ) 
 
            save_appointments() 
 
            st.success( 
                f"Appointment booked on " 
                f"{date_text} at {time_text}" 
            ) 
 
 
# ========================================================= 
# APPOINTMENT CANCELLATION 
# ========================================================= 
 
elif menu == "Appointment Cancellation": 
 
    st.header("❌ Appointment Cancellation") 
 
    booked = [ 
 
        a 
        for a in st.session_state.appointments 
        if a["status"] == "Booked" 
 
    ] 
 
    if not booked: 
 
        st.info("No booked appointments found.") 
 
    else: 
 
        options = [] 
 
        for appointment in booked: 
 
            options.append( 
                f"{appointment['patient_id']} - " 
                f"{appointment['doctor_id']} - " 
                f"{appointment['date']} - " 
                f"{appointment['time']}" 
            ) 
 
        selected = st.selectbox( 
            "Select Appointment", 
            options 
        ) 
 
        index = options.index(selected) 
 
        appointment = booked[index] 
 
        if st.button( 
            "Cancel Appointment", 
            type="primary" 
        ): 
 
            appointment["status"] = "Cancelled" 
 
            save_appointments() 
 
            st.success( 
                "Appointment cancelled successfully!" 
            ) 
 
 
# ========================================================= 
# MEDICAL HISTORY 
# ========================================================= 
 
elif menu == "Medical History": 
 
    st.header("📋 Medical History") 
 
    if not st.session_state.patients: 
 
        st.info("No patients registered.") 
 
    else: 
 
        patient_ids = [ 
            p["id"] 
            for p in st.session_state.patients 
        ] 
 
        patient_id = st.selectbox( 
            "Select Patient", 
            patient_ids 
        ) 
 
        patient = find_patient(patient_id) 
 
        # Fix old patient records 
        if "history" not in patient: 
            patient["history"] = [] 
 
        treatment = st.text_area( 
            "Enter Treatment / Medical History" 
        ) 
 
        if st.button( 
            "Add Medical History", 
            type="primary" 
        ): 
 
            if not treatment.strip(): 
 
                st.warning( 
                    "Please enter treatment details." 
                ) 
 
            else: 
 
                record = ( 
                    datetime.now().strftime("%d-%m-%Y") 
                    + " : " 
                    + treatment 
                ) 
 
                patient["history"].append(record) 
 
                save_patients() 
 
                st.success( 
                    "Medical history added successfully!" 
                ) 
 
        st.subheader("Previous Records") 
 
        if patient["history"]: 
 
            for record in patient["history"]: 
 
                st.write("•", record) 
 
        else: 
 
            st.info("No medical history records.") 
 
 
# ========================================================= 
# CONSULTATION CHARGES 
# ========================================================= 
 
elif menu == "Consultation Charges": 
 
    st.header("💰 Consultation Charges") 
 
    if not st.session_state.doctors: 
 
        st.info("No doctors registered.") 
 
    else: 
 
        doctor_ids = [ 
            d["id"] 
            for d in st.session_state.doctors 
        ] 
 
        doctor_id = st.selectbox( 
            "Select Doctor", 
            doctor_ids 
        ) 
 
        doctor = find_doctor(doctor_id) 
 
        col1, col2, col3 = st.columns(3) 
 
        col1.metric( 
            "Doctor", 
            doctor["name"] 
        ) 
 
        col2.metric( 
            "Specialization", 
            doctor["specialization"] 
        ) 
 
        col3.metric( 
            "Consultation Charge", 
            f"₹{doctor['charge']}" 
        ) 
 
 
# ========================================================= 
# BILLING 
# ========================================================= 
 
elif menu == "Billing": 
 
    st.header("🧾 Hospital Billing") 
 
    if not st.session_state.patients: 
 
        st.info("No patients registered.") 
 
    else: 
 
        patient_ids = [ 
            p["id"] 
            for p in st.session_state.patients 
        ] 
 
        patient_id = st.selectbox( 
            "Select Patient", 
            patient_ids 
        ) 
 
        patient = find_patient(patient_id) 
 
        if not patient["doctor"]: 
 
            st.warning( 
                "No doctor allocated to this patient." 
            ) 
 
        else: 
 
            doctor = None 
 
            for d in st.session_state.doctors: 
 
                if d["name"] == patient["doctor"]: 
 
                    doctor = d 
 
                    break 
 
            if doctor: 
 
                st.divider() 
 
                st.subheader( 
                    "🏥 HOSPITAL BILL" 
                ) 
 
                st.write( 
                    "**Patient ID:**", 
                    patient["id"] 
                ) 
 
                st.write( 
                    "**Patient Name:**", 
                    patient["name"] 
                ) 
 
                st.write( 
                    "**Doctor:**", 
                    doctor["name"] 
                ) 
 
                st.write( 
                    "**Specialization:**", 
                    doctor["specialization"] 
                ) 
 
                st.write( 
                    "**Consultation Charge:**", 
                    f"₹{doctor['charge']}" 
                ) 
 
                st.write( 
                    "**Date:**", 
                    datetime.now().strftime( 
                        "%d-%m-%Y" 
                    ) 
                ) 
 
                st.divider() 
 
                st.markdown( 
                    f"## Total Bill: ₹{doctor['charge']}" 
                ) 
 
 
# ========================================================= 
# PATIENT SEARCH 
# ========================================================= 
 
elif menu == "Patient Search": 
 
    st.header("🔍 Patient Search") 
 
    patient_id = st.text_input( 
        "Enter Patient ID" 
    ) 
 
    if st.button( 
        "Search Patient", 
        type="primary" 
    ): 
 
        patient = find_patient(patient_id) 
 
        if patient: 
 
            st.success("Patient found!") 
 
            col1, col2, col3 = st.columns(3) 
 
            col1.metric( 
                "Patient ID", 
                patient["id"] 
            ) 
 
            col2.metric( 
                "Age", 
                patient["age"] 
            ) 
 
            col3.metric( 
                "Doctor", 
                patient["doctor"] 
                if patient["doctor"] 
                else "Not Allocated" 
            ) 
 
            st.write( 
                "**Name:**", 
                patient["name"] 
            ) 
 
            st.write( 
                "**Phone:**", 
                patient["phone"] 
            ) 
 
            st.subheader( 
                "📋 Medical History" 
            ) 
 
            if patient["history"]: 
 
                for record in patient["history"]: 
 
                    st.write( 
                        "•", 
                        record 
                    ) 
 
            else: 
 
                st.info( 
                    "No medical history." 
                ) 
 
        else: 
 
            st.error( 
                "Patient not found!" 
            ) 
 
 
# ========================================================= 
# DAILY APPOINTMENT REPORT 
# ========================================================= 
 
elif menu == "Daily Appointment Report": 
 
    st.header("📊 Daily Appointment Report") 
 
    selected_date = st.date_input( 
        "Select Date", 
        value=date.today() 
    ) 
 
    selected_date_text = selected_date.strftime( 
        "%d-%m-%Y" 
    ) 
 
    appointments = [ 
 
        a 
        for a in st.session_state.appointments 
 
        if a["date"] == selected_date_text 
 
    ] 
 
    st.write( 
        f"### Appointments on {selected_date_text}" 
    ) 
 
    if not appointments: 
 
        st.info( 
            "No appointments for this date." 
        ) 
 
    else: 
 
        for appointment in appointments: 
 
            patient = find_patient( 
                appointment["patient_id"] 
            ) 
 
            doctor = find_doctor( 
                appointment["doctor_id"] 
            ) 
 
            with st.container(border=True): 
 
                col1, col2, col3, col4 = st.columns(4) 
 
                col1.write( 
                    "**Patient**" 
                ) 
 
                col1.write( 
                    patient["name"] 
                    if patient 
                    else appointment["patient_id"] 
                ) 
 
                col2.write( 
                    "**Doctor**" 
                ) 
 
                col2.write( 
                    doctor["name"] 
                    if doctor 
                    else appointment["doc               tor_id"] 
                ) 
 
                col3.write( 
                    "**Time**" 
                ) 
 
                col3.write( 
                    appointment["time"] 
                ) 
 
                col4.write( 
                    "**Status**" 
                ) 
 
                col4.write( 
                    appointment["status"] 
                ) 