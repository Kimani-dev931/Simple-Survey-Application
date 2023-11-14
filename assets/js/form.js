let currentTab = 0;
    showTab(currentTab);

    function showTab(n) {
        const tabs = document.getElementsByClassName("tab");
        const submitBtn = document.getElementById("submitBtn");


        tabs[n].style.display = "block";


        if (n === 0) {
            document.getElementById("prevBtn").style.display = "none";
        } else {
            document.getElementById("prevBtn").style.display = "inline";
        }

        if (n === tabs.length - 1) {
            document.getElementById("nextBtn").style.display = "none";
            submitBtn.style.display = "inline";
        } else {
            document.getElementById("nextBtn").style.display = "inline";
            submitBtn.style.display = "none";
        }


        fixStepIndicator(n);
    }

    function nextPrev(n) {
        const tabs = document.getElementsByClassName("tab");


        if (n === 1 && !validateForm()) return false;


        tabs[currentTab].style.display = "none";


        currentTab += n;


        if (currentTab >= tabs.length) {
            document.getElementById("regForm").submit();
            return false;
        }


        showTab(currentTab);
    }

    function validateForm() {
        const tabs = document.getElementsByClassName("tab");
        const inputs = tabs[currentTab].getElementsByTagName("input");


        for (let i = 0; i < inputs.length; i++) {
            if (inputs[i].value === "") {
                inputs[i].className += " invalid";
                return false;
            }
        }


        document.getElementsByClassName("step")[currentTab].className += " finish";
        return true;
    }

    function fixStepIndicator(n) {
        const steps = document.getElementsByClassName("step");
        for (let i = 0; i < steps.length; i++) {
            steps[i].className = steps[i].className.replace(" active", "");
        }
        steps[n].className += " active";
    }

   $(document).ready(function() {
      $('#successModal').modal('show');
    });
