from qiskit_ibm_runtime import QiskitRuntimeService
import os
from dotenv import load_dotenv


load_dotenv() 

my_api_key = os.getenv("API_KEY")

QiskitRuntimeService.save_account(
    # For `token`, use the 44-character API_KEY you created
    # and saved from the IBM Quantum Platform Home dashboard
    token=my_api_key ,
    overwrite=True
)

# Run every time you need the service
service = QiskitRuntimeService()
print("Success")