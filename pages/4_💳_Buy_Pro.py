import streamlit as st

st.set_page_config(page_title="💳 Buy Pro - RoleMatrix.AI", layout="wide")

st.title("💳 Upgrade to RoleMatrix Pro")
st.markdown("Unlock access to premium features like SoD conflict export.")

# Correct script injection format
html_code = f"""
<html>
<head><script src="https://checkout.razorpay.com/v1/checkout.js"></script></head>
<body>
  <button id="rzp-button1" style="padding: 10px 20px; background-color: #635bff; color: white; border: none; border-radius: 8px;">Buy Pro – ₹49</button>
  <script>
    var options = {{
        "key": "rzp_test_1234567890abcdef",  // 🔁 Replace with rzp_live_xxxx
        "amount": "4900",
        "currency": "INR",
        "name": "RoleMatrix.AI",
        "description": "Pro Access (1 Month)",
        "handler": function (response) {{
            alert("Payment successful: " + response.razorpay_payment_id);
        }}
    }};
    var rzp1 = new Razorpay(options);
    document.getElementById('rzp-button1').onclick = function(e){{
        rzp1.open();
        e.preventDefault();
    }}
  </script>
</body>
</html>
"""

st.components.v1.html(html_code, height=300)
