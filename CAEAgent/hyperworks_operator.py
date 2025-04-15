import os  # Added for PATH checks
import subprocess  # Added import for subprocess module
import hm  # Import hm module for HyperWorks operations

class HyperWorksOperator:
    def __init__(self, model_path):
        self.model_path = model_path

    def open_hyperworks(self):
        """Open HyperMesh."""
        try:
            # Check if 'hw' command is available
            result = subprocess.run(['hmopengl', '-version'], capture_output=True, text=True, check=True)
            # If 'hw' is available, open HyperWorks
            subprocess.run(['hmopengl'])
            # print("HyperWorks opened successfully.")
        except subprocess.CalledProcessError:
            raise FileNotFoundError('HyperWorks CLI tool (hw) not found. Please ensure HyperWorks is installed and added to your system PATH.')

    def import_bdf(self):
        """Import a BDF file into HyperMesh using a TCL script."""
        try:

            # Call HyperWorks with the TCL script directly
            subprocess.run(['hmopengl','-tcl','./TCL/import_bdf.tcl'])
            # print("BDF file imported successfully.")

        except subprocess.CalledProcessError:
            raise FileNotFoundError('HyperWorks CLI tool (hw) not found. Please ensure HyperWorks is installed and added to your system PATH.')
