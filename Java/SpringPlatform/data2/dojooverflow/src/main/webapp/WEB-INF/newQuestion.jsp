<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%> 
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>New Question</title>
</head>
<body>
<h1>New Question</h1>
<p><form:errors path="question.*"/></p>
<form:form action="/questions/new" method="post" modelAttribute="question">
    <p>
        <form:label path="question">Question:</form:label>
        <form:textarea path="question"/>
    </p>
    <p>
        <form:label path="tags">Tags:</form:label>
        <form:input path="tags"/>
    </p>
    <input type="submit" value="Submit"/>
</form:form>
</body>
</html>