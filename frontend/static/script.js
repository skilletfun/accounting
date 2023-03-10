function createRowOfInputs(data, keys, widths, name){
    var row = document.createElement('div');
    row.className = 'row';
    if (typeof name != "undefined") row.name = name;
    for (var j = 0; j < keys.length; j++){
        var obj = document.createElement('div');
        obj.className= 'col-' + widths[j];
        inp = document.createElement('input');
        inp.className = 'form-control';
        inp.value = data[keys[j]];
        inp.name = keys[j];
        inp.type = 'text';
        inp.disabled = true;
        inp.readonly = true;
        obj.appendChild(inp);
        row.appendChild(obj);
    }
    return row;
}

function createButton(name, func){
    btn = document.createElement('button');
    btn.style = "margin:auto;border-color:transparent;background-color:transparent;"
    icon = document.createElement("i");
    icon.className = "fa fa-" + name + " fa-2x";
    btn.appendChild(icon);
    btn.onclick = func;
    return btn;
}

function collectData(row){
    var data = {};
    for (var i = 1; i < row.children.length; i++)
    {
        var inp_obj = row.children[i].firstChild;
        if (inp_obj.parentElement.className.startsWith("col-") && inp_obj.tagName == "INPUT")
        {
            inp_obj.disabled = true;
            data[inp_obj.name] = inp_obj.value;
        }
        if (inp_obj.parentElement.className.startsWith("collapse"))
        {
            for (var j = 0; j < inp_obj.children.length; j++)
            {
                if (inp_obj.children[j].className == "row")
                {
                    data[inp_obj.children[j].name] = collectData(inp_obj.children[j]);
                }
            }
        }
    }
    return data;
}

function disableRow(row){
    for (var i = 1; i < row.children.length; i++)
    {
        var inp_obj = row.children[i].firstChild;
        if (inp_obj.parentElement.className.startsWith("col") && inp_obj.tagName == "INPUT")
        {
            inp_obj.disabled = true;
        }
    }
}

function editRowData(obj){
    var row = obj.parentElement.parentElement;
    var index = row.firstChild.firstChild.value;
    if (!row.children[1].firstChild.disabled) // Запретить редактирование и отправить запрос
    {
        var data = {};
        var xhr = new XMLHttpRequest();
        if (index == "")
        {
            if (row.getAttribute("root") == "true") // Создать запись
            {
                data = collectData(row);
                var url = "http://0.0.0.0:8000/" + row.getAttribute('apiurl');
                xhr.open("PUT", url, true);
                xhr.setRequestHeader('Content-type', 'application/json');
                xhr.send(JSON.stringify(data));
            }
            disableRow(row);
        }
        else // Обновить запись
        {
            for (var i = 1; i < row.children.length-1; i++)
            {
                var inp_obj = row.children[i].firstChild;
                if (inp_obj.parentElement.className.startsWith("col"))
                {
                    inp_obj.disabled = true;
                    data[inp_obj.name] = inp_obj.value;
                }
            }
            var url = "http://0.0.0.0:8000/" + row.getAttribute('apiurl') + '/' + index;
            xhr.open("POST", url, true);
            xhr.setRequestHeader('Content-type', 'application/json');
            xhr.send(JSON.stringify(data));
        }
    }
    else // Разрешить редактирование
    {
        for (var i = 1; i < row.children.length-1; i++)
        {
            row.children[i].firstChild.disabled = false;
        }
    }
}

function deleteObj(btn){
    var row = btn.parentElement.parentElement;
    var index = row.firstChild.firstChild.value;
    if (index != "")
    {
        var url = "http://0.0.0.0:8000/" + row.getAttribute('apiurl') + '/' + index;
        var xhr = new XMLHttpRequest();
        xhr.open("DELETE", url, true);
        xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        xhr.send();
    }
    row.remove();
}

function createControlButtons(row, apiURL, label, add_trash){
    var obj = document.createElement('div');
    row.setAttribute('apiurl', apiURL);
    obj.className= 'col-1';
    edit = createButton("pencil", function(){editRowData(this);});
    obj.appendChild(edit);
    if (typeof label !== 'undefined')
    {
        collapse = createButton("caret-down", function(){});
        collapse.setAttribute('data-bs-toggle', "collapse");
        collapse.setAttribute('aria-expanded', "false");
        collapse.setAttribute('data-bs-target', "#"+label);
        collapse.setAttribute('aria-controls', label);
        obj.appendChild(collapse);
    }
    if (typeof add_trash !== 'undefined')
    {
        trash = createButton("trash-o", function(){deleteObj(this);});
        obj.appendChild(trash);
    }
    row.appendChild(obj);
    return obj;
}

function createHiddenBlock(label, lables, objects){
    collapse = document.createElement('div');
    collapse.className = "collapse";
    collapse.id = label;
    card = document.createElement('div');
    card.className = "card card-body";
    for (var i = 0; i < objects.length; i++){
        var p = document.createElement('p');
        p.textContent = lables[i];
        card.appendChild(p);
        card.appendChild(objects[i]);
    }
    collapse.appendChild(card);
    return collapse;
}

//          LOADING TABS

function loadUsers(){
    var url = "http://0.0.0.0:8000/users";
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url, true);
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhr.setRequestHeader('Access-Control-Allow-Private-Network', true);
    xhr.onload = function() {
        var data = JSON.parse(this.responseText)["users"];
        document.getElementById('users').replaceChildren();
        var header = document.createElement('div');
        header.className = 'row';
        var header_data = ["ID", "Имя", "Фамилия", "Отчество", "Адрес"]
        var header_widths = ['1', '2', '2', '2', '4'];
        for (var k = 0; k < header_widths.length; k++){
            var obj = document.createElement('div');
            obj.className= 'col-' + header_widths[k];
            var p = document.createElement('p');
            p.style = "text-align: center;";
            p.textContent = header_data[k];
            obj.appendChild(p);
            header.appendChild(obj);
        }
        document.getElementById('users').appendChild(header);
        for (var i = 0; i < data.length; i++){
            var user = createUser(
                [
                    data[i],
                    ['id', 'name', 'surname', 'patronimic', 'address'],
                    ['1', '2', '2', '2', '4']
                ],
                [
                    data[i]["passport"],
                    ['id', 'series', 'number', 'givenBy', 'registerAddress', 'birthdayAddress'],
                    ['1', '1', '1', '2', '3', '3']
                ],
                [
                    data[i]["inn"],
                    ['id', 'series', 'number', 'givenBy'],
                    ['1', '1', '1', '2']
                ],
                [
                    data[i]["snils"],
                    ['id', 'series', 'number', 'givenBy'],
                    ['1', '1', '1', '2']
                ],
                i,
                data[i]["drives"]
            );
            user.setAttribute("root", true);
            document.getElementById('users').appendChild(user);
        }
    };
    xhr.send();
}

function loadDrives(){
    var url = "http://0.0.0.0:8000/drives";
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url, true);
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhr.setRequestHeader('Access-Control-Allow-Private-Network', true);
    xhr.onload = function() {
        var data = JSON.parse(this.responseText)["drives"];
        document.getElementById('drives').replaceChildren();
        var header = document.createElement('div');
        header.className = 'row';
        var header_data = ["ID", "Тип", "Номер", "Дата выдачи", "Принят", "Уничтожен", "Дата уничтожения", "Документ об уничтожении"]
        var header_widths = ['1', '2', '2', '1', '1', '1', '1', '2'];
        for (var k = 0; k < header_widths.length; k++){
            var obj = document.createElement('div');
            obj.className= 'col-' + header_widths[k];
            var p = document.createElement('p');
            p.style = "text-align: center;";
            p.textContent = header_data[k];
            obj.appendChild(p);
            header.appendChild(obj);
        }
        document.getElementById('drives').appendChild(header);
        for (var i = 0; i < data.length; i++){
            var row = createDrive(data[i]);
            document.getElementById('drives').appendChild(row);
        }
    };
    xhr.send();
}

//          CREATE ENTITY

function createUser(user, passport_data, inn_data, snils_data, i, drives){
    var row = createRowOfInputs(user[0], user[1], user[2]);
    row.setAttribute("root", true);
    createControlButtons(row, 'users', "user-"+String(i), true);
    var passport = createRowOfInputs(passport_data[0], passport_data[1], passport_data[2], "passport");
    createControlButtons(passport, 'users/passport');
    var inn = createRowOfInputs(inn_data[0], inn_data[1], inn_data[2], "inn");
    createControlButtons(inn, 'users/inn');
    var snils = createRowOfInputs(snils_data[0], snils_data[1], snils_data[2], "snils");
    createControlButtons(snils, 'users/snils');
    collapse = createHiddenBlock("user-"+String(i), ["Паспорт", "ИНН", "СНИЛС"], [passport, inn, snils]);
    var p = document.createElement('p');
    p.textContent = "Носители";
    collapse.firstChild.appendChild(p);
    if (typeof drives != "undefined")
    {
        var ol = document.createElement('ol');
        ol.className = "list-group list-group-numbered";
        for (var j = 0; j < drives.length; j++)
        {
            var li = document.createElement('li');
            li.className = "list-group-item";
            li.textContent = drives[j]["type"] + " " + drives[j]["number"];
            ol.appendChild(li);
        }
        collapse.firstChild.appendChild(ol);
    }
    row.appendChild(collapse);
    return row;
}

function createEmptyUser(){
    var user = createUser(
        [
            {'id': '', 'name': '', 'surname': '', 'patronimic': '', 'address': ''},
            ['id', 'name', 'surname', 'patronimic', 'address'],
            ['1', '2', '2', '2', '4']
        ],
        [
            {'id': '', 'series': '', 'number': '', 'givenBy': '', 'registerAddress': '', 'birthdayAddress': ''},
            ['id', 'series', 'number', 'givenBy', 'registerAddress', 'birthdayAddress'],
            ['1', '1', '1', '2', '3', '3']
        ],
        [
            {'id': '', 'series': '', 'number': '', 'givenBy': ''},
            ['id', 'series', 'number', 'givenBy'],
            ['1', '1', '1', '2']
        ],
        [
            {'id': '', 'series': '', 'number': '', 'givenBy': ''},
            ['id', 'series', 'number', 'givenBy'],
            ['1', '1', '1', '2']
        ],
        document.getElementById('users').children.length+1
    );
    document.getElementById('users').appendChild(user);
}

function createDrive(data){
    var row = createRowOfInputs(
        data,
        ['id', 'type', 'number', 'givenDate', 'isAccepted', 'isDestroyed', 'destroyDate', 'destroyDocument'],
        ['1', '2', '2', '1', '1', '1', '1', '2']
    );
    row.setAttribute("root", true);
    var obj = createControlButtons(row, 'drives');
    trash = createButton("trash-o", function(){deleteObj(this);});
    obj.appendChild(trash);
    var btn = createButton("user", function(){setUsersToModal(this);});
    btn.setAttribute("data-bs-toggle", "modal");
    btn.setAttribute("data-bs-target", "#selectUserModal");
    obj.insertBefore(btn, obj.firstChild);
    return row;
}

function setUsersToModal(btn){
    var url = "http://0.0.0.0:8000/users";
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url, true);
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhr.onload = function(){
        var data = JSON.parse(this.responseText)["users"];
        var s = document.getElementById('userSelect');
        s.setAttribute("drive-id", btn.parentElement.parentElement.firstChild.firstChild.value);
        s.replaceChildren();
        var def_opt = document.createElement("option");
        def_opt.value = "-1";
        def_opt.textContent = "Не выбрано";
        s.appendChild(def_opt);
        for (var i = 0; i < data.length; i++)
        {
            var obj = document.createElement("option");
            obj.value = data[i]["id"];
            obj.textContent = data[i]["name"] + " " + data[i]["surname"] + " " + data[i]["patronimic"];
            s.appendChild(obj);
        }
    }
    xhr.send();
}

function addDriveToUser(){
    var value = document.getElementById('userSelect').value;
    if (value != "-1")
    {
        var url = "http://0.0.0.0:8000/drives/user/?drive_id=" + document.getElementById('userSelect').getAttribute("drive-id") + "&user_id="+value;
        var xhr = new XMLHttpRequest();
        xhr.open("POST", url, true);
        xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        xhr.send();
    }
    else
    {
        var url = "http://0.0.0.0:8000/drives/user/?drive_id=" + document.getElementById('userSelect').getAttribute("drive-id");
        var xhr = new XMLHttpRequest();
        xhr.open("DELETE", url, true);
        xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        xhr.send();
    }
}

function createEmptyDrive(){
    var drive = createDrive({'id': '', 'type': '', 'number': '', 'givenDate': '', 'isAccepted': '', 'isDestroyed': '', 'destroyDate': '', 'destroyDocument': ''});
    document.getElementById('drives').appendChild(drive);
}

function createEmptyEntity(){
    var tabs = document.getElementById("pills-tab").children;
    for (var i = 0; i < tabs.length; i++)
    {
        if (tabs[i].getElementsByTagName("button")[0].className.endsWith("active"))
        {
            var obj = tabs[i].getElementsByTagName("button")[0].getAttribute("aria-controls");
            if (obj == "users") createEmptyUser();
            if (obj == "drives") createEmptyDrive();
        }
    }
}