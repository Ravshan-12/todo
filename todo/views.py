from django.http import HttpResponse

def task_list(request):
    html_content = """ 
            <!DOCTYPE html>
    <html lang="uz">
    <head>
        <meta charset="UTF-8">
        <title>Vazifalar Ro'yxati</title>
    </head>
    <body>
        <h1>Vazifalar Ro'yxati</h1>
        <h2>Yangi vazifa qo'shish</h2>
        <form id="taskForm">
            Vazifa nomi: <input type="text" id="taskName" required><br>
            Tavsif: <textarea id="taskDescription" required></textarea><br>
            Muhimlik darajasi: 
            <select id="taskPriority" required>
                <option>Past</option>
                <option>O'rta</option>
                <option>Yuqori</option>
            </select><br>
            Muddat: <input type="date" id="taskDeadline" required><br>
            <button type="submit">Vazifani qo'shish</button>
        </form>

        <h2>Mavjud vazifalar</h2>
        <table id="taskTable" border="1">
            <tr>
                <th>Vazifa</th>
                <th>Tavsif</th>
                <th>Muhimlik</th>
                <th>Muddat</th>
                <th>Holat</th>
            </tr>
            <tr>
                <td>Hisobot tayyorlash</td>
                <td>Oylik moliyaviy hisobotni tayyorlash va topshirish</td>
                <td>Yuqori</td>
                <td>2023-05-31</td>
                <td>Bajarilmoqda</td>
            </tr>
            <tr>
                <td>Mijoz bilan uchrashuv</td>
                <td>Yangi loyiha bo'yicha mijoz bilan muzokaralar o'tkazish</td>
                <td>O'rta</td>
                <td>2023-05-25</td>
                <td>Rejalashtirilgan</td>
            </tr>
            <tr>
                <td>Prezentatsiya tayyorlash</td>
                <td>Yangi mahsulot uchun taqdimot slaydlarini tayyorlash</td>
                <td>Past</td>
                <td>2023-06-05</td>
                <td>Boshlanmagan</td>
            </tr>
            <tr>
                <td>Xodimlar uchun trening</td>
                <td>Yangi dasturiy ta'minot bo'yicha xodimlarga qo'llanma berish</td>
                <td>O'rta</td>
                <td>2023-06-10</td>
                <td>Rejalashtirilgan</td>
            </tr>
        </table>

        <script>
            document.getElementById('taskForm').addEventListener('submit', function(event) {
                event.preventDefault(); // Form yuborilishini to'xtatish

                const taskName = document.getElementById('taskName').value;
                const taskDescription = document.getElementById('taskDescription').value;
                const taskPriority = document.getElementById('taskPriority').value;
                const taskDeadline = document.getElementById('taskDeadline').value;

                const table = document.getElementById('taskTable');
                const row = table.insertRow(-1); // Jadval oxiriga qator qo'shish
                row.innerHTML = `
                    <td>${taskName}</td>
                    <td>${taskDescription}</td>
                    <td>${taskPriority}</td>
                    <td>${taskDeadline}</td>
                    <td>Boshlanmagan</td>
                `;

                document.getElementById('taskForm').reset(); // Formani tozalash
            });
        </script>
    </body>
    </html>
     """
    return HttpResponse(html_content)