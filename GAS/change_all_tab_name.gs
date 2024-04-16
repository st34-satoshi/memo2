function myFunction() {
  const sheets = SpreadsheetApp.getActiveSpreadsheet().getSheets();
  for (const sheet of sheets) {
    const current_name = sheet.getSheetName();
    console.log(current_name);
    const new_name = current_name.replace('2020', '2024');
    console.log(new_name);
    sheet.setName(new_name);
  }
}
