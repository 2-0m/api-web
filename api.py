"""
<center> 
    <div class="container">
        <div class="hamburger" onclick="toggleSidebar()">
            <img src="https://icon-icons.com/downloadimage.php?id=184615&root=2954/PNG/512/&file=three_dots_vertical_menu_icon_184615.png" class="menu-icon"/>
        </div>
        <div class="sidebar" id="sidebar">
            <ul>
                <li><a href="https://github.com/i0i1" target="_blank" rel="noopener noreferrer">𝙂𝙞𝙩𝙝𝙪𝙗</a></li>
                <li><a href="https://telegram.dog/GTT_G">𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢</a></li>
                <li><a href="https://www.instagram.com/5__d_">𝙄𝙣𝙨𝙩𝙖𝙜𝙧𝙖𝙢</a></li>
            </ul>
        </div>
        <div class="content">
            <img src="https://i.giphy.com/media/3o7abAHdYvZdBNnGZq/giphy.webp" class="circular-image"/> 
            <p class="text">Mustafa Abbas</p>
            <a href="https://t.me/GTT_G" class="button-link">
                <button class="button">Coder</button>
            </a>
        </div>
    </div>
</center> 
<style>
    body { 
        background:antiquewhite;
        font-family: Arial, sans-serif;
    }
    .container {
        background: #f5f5dc;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        display: flex;
        flex-direction: column;
        text-align: center;
        width: 70%;
        margin: auto;
        position: relative;
    }
    .hamburger {
        cursor: pointer;
        position: absolute;
        top: 10px;
        left: 10px;
    }
    .menu-icon {
        width: 30px;
        height: 30px;
    }
    .sidebar {
        position: absolute;
        top: 50px;
        left: 10px;
        width: 200px;
        max-height: 0;
        overflow: hidden;
        background-color: #fff;
        border-radius: 12px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        transition: max-height 0.3s;
        z-index: 1;
    }
    .sidebar ul {
        list-style-type: none;
        padding: 0;
        margin: 0;
        width: 100%;
    }
    .sidebar ul li {
        margin-bottom: 10px;
        text-align: center;
        width: 100%;
    }
    .sidebar ul li a {
        text-decoration: none;
        color: #333;
        font-size: 16px;
        display: block;
        padding: 10px 0;
        transition: background-color 0.3s, color 0.3s;
    }
    .sidebar ul li a:hover {
        background-color: #f0f0f0;
        color: red;
    }
    .content {
        padding-top: 50px;
        flex-grow: 1;
    }
    .circular-image {
        border-radius: 50%;
        width: 200px;
        height: 200px;
        border: 5px solid #333;
    }
    .text {
        font-size: 20px;
        color: #333;
        margin-top: 15px;
    }
    .button-link {
        text-decoration: none;
    }
    .button {
        padding: 10px 20px;
        font-size: 16px;
        border-radius: 5px;
        border: none;
        background-color: #333;
        color: #fff;
        cursor: pointer;
        margin-top: 10px;
        transition: background-color 0.3s ease;
    }
    .button:active {
        background-color: red;
    }
</style>
<script>
    function toggleSidebar() {
        var sidebar = document.getElementById("sidebar");
        if (sidebar.style.maxHeight === "0px") {
            sidebar.style.maxHeight = "200px";
        } else {
            sidebar.style.maxHeight = "0px";
        }
    }
    document.addEventListener("click", function(event) {
        var sidebar = document.getElementById("sidebar");
        var hamburger = document.querySelector(".hamburger");
        if (sidebar.style.maxHeight === "200px" && !sidebar.contains(event.target) && !hamburger.contains(event.target)) {
            sidebar.style.maxHeight = "0px";
        }
    });

    document.onkeydown = function (e) {
        if (event.keyCode == 123) {
            return false;
        }
       if (e.ctrlKey && e.shiftKey && e.keyCode == 'I'.charCodeAt(0)) {
            return false;
        }
        if (e.ctrlKey && e.shiftKey && e.keyCode == 'C'.charCodeAt(0)) {
            return false;
        }
        if (e.ctrlKey && e.shiftKey && e.keyCode == 'J'.charCodeAt(0)) {
            return false;
        }
        if (e.ctrlKey && e.keyCode == 'U'.charCodeAt(0)) {
            return false;
        }
    }
</script>"""