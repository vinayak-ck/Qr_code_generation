document.getElementById('generate').addEventListener('click', function() {
    const upiId = document.getElementById('upi-id').value;

    if (!upiId) {
        alert('Please enter a UPI ID');
        return;
    }

    const qrCodesContainer = document.getElementById('qr-codes');
    qrCodesContainer.innerHTML = ''; // Clear previous QR codes

    const paymentApps = ['PhonePe', 'Paytm', 'Google Pay'];

    paymentApps.forEach(app => {
        const qrCodeUrl = `upi://pay?pa=${upiId}&pn=Recipient%20Name&mc=1234`;

        const qrCodeElement = document.createElement('img');
        qrCodeElement.src = `https://api.qrserver.com/v1/create-qr-code/?data=${encodeURIComponent(qrCodeUrl)}&size=100x100`;
        qrCodeElement.alt = `${app} QR Code`;
        qrCodeElement.className = 'qr-code';

        qrCodesContainer.appendChild(qrCodeElement);
    });
});
