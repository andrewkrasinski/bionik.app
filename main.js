download.addEventListener('click', function() {
    var doc = new jsPDF()
    doc.text(10, 10, doc.splitTextToSize(text.value, 180));
    doc.save('doc.pdf');
})