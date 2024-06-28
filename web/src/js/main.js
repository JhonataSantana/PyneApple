function getElement(selector) {
    return document.querySelector(selector)
}

function addLeadingZeros(num, targetLength) {

    let numStr = num.toString();

    while (numStr.length < targetLength) {

        numStr = '0' + numStr;

    }

    return numStr;

}

function removeFileExtension(filename){
    return filename.split(".")[0]
}

function createMaterialIcon(icon){
    const span = document.createElement("span");
    span.classList.add("material-symbols-outlined");
    span.innerHTML = icon;
    return span
}

function creatFileListItem(filename, index){

    const li = document.createElement("li")
    li.classList.add("list-group-item", "d-flex", "justify-content-between", "align-items-center", "p-3");
    const label = document.createElement("label")
    label.classList.add("lbl_checkbox", "d-flex", "align-items-center", "m-0");
    label.setAttribute("for", `${removeFileExtension(filename)}${index}`);
    const input = document.createElement("input");
    input.setAttribute("id", `${removeFileExtension(filename)}${index}`);
    input.setAttribute("value", filename);
    input.setAttribute("type", "checkbox");
    const check_icon_1 = createMaterialIcon('check_box');
    const check_icon_2 = createMaterialIcon('check_box_outline_blank');
    const span = document.createElement('span')
    span.classList.add("flex-grow-1", "mx-3");
    span.innerHTML = filename;

    li.appendChild(label)
    li.appendChild(span);
    label.appendChild(input)
    label.appendChild(check_icon_1)
    label.appendChild(check_icon_2);

    return li
}

function updateFileList(files){

    file_list_counter.innerHTML = files.length > 0 ? `Foram encontrado(s) ${files.length} arquivo(s)` : "Nenhum aquivo encontrado"
    file_list.innerHTML = "";

    const fragment = document.createDocumentFragment();

    files.forEach((file, index) => {fragment.appendChild(creatFileListItem(file, index))});

    file_list.appendChild(fragment);

}

// Setting first form elements
const origin_path_input = getElement('#origin_path');
const origin_path_btn = getElement('#origin_path_btn');
const substring_input = getElement("#substring");
const start_date_input = getElement("#start_date");
const end_date_input = getElement("#end_date");
const search_files_btn = getElement("#search_files");

// Setting second form elements
const file_list_counter = getElement(".file_list_counter");
const file_list = getElement(".file_list");

// Setting Inputs
const today = new Date();
const year = today.getFullYear();
const month = today.getMonth() + 1;
const day = today.getDate();
const today_str = `${year}-${addLeadingZeros(month, 2)}-${addLeadingZeros(day, 2)}`;

start_date_input.max = today_str;
end_date_input.max = today_str;

// Setting Triggers
origin_path_btn.addEventListener("click", async () => {
    const origin_path = await eel.getOriginPath()();
    origin_path_input.value = origin_path;
});

search_files_btn.addEventListener("click", async () => {
    const folder_data = await eel.getFolderData(origin_path_input.value, substring_input.value, start_date_input.value, end_date_input.value)();
    updateFileList(folder_data);
});





// console.log("Calling Python...");
// async function teste() {
//     let t = await eel.my_python_function(1, 2)();
//     console.log(t)
// }

// teste()

// eel.expose(my_javascript_function);
// function my_javascript_function(a, b, c, d) {
//     if (a < b) {
//         console.log(c * d);
//     }
// }
