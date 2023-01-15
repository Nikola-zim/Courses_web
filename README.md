КРАТКОЕ СОДЕРЖАНИЕ

На базе фреймворка Django разработать веб-приложение, представляющее собой учебный портал по курсу "Фреймворк Zend". Портал должен содержать достаточное количество учебного материала (статей, разделов, подразделов, описание процесса разработки и т.п.)  с примерами для успешного освоения заданной темы.

АРХИТЕКТУРА ПРОЕКТА

Архитектура Django похожа на «Модель-Представление-Контроллер» (MVC). Контроллер классической модели MVC примерно соответствует уровню, который в Django называется Представление (англ. View), а презентационная логика Представления реализуется в Django уровнем Шаблонов (англ. Template). 

ОПИСАНМИЕ ФУНКЦИОНАЛА

Проект содержит два веб-приложения, первое вспомогательное приложение предназначено для выбора нужного курса из предложенных и содержит главную страницу проекта. По нажатию на контейнер с описанием и обложкой курса, пользователь переходит к основному веб-приложению, в котором представлены материалы конкретного курса.

![image](https://user-images.githubusercontent.com/81438725/212570796-c75556ad-fc73-4579-bbaf-d2824b141802.png)