<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
    <%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%> 
    
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Dashboard</title>
</head>
<body>
	<table>
    <thead>
    	<tr>
            <th>Name</th>
            <th>Creator</th>
            <th>Version</th>
            <th>Action</th>
        </tr>
    </thead>
    <tbody>
    	<c:forEach items="${languages}" var="lang">
        <tr>
            <td><a href="/languages/${lang.id}">${lang.name}</a></td>
            <td>${lang.creator}</td>
            <td>${lang.version}</td>
            <td>
                <a href="/languages/${lang.id}/edit">Edit</a>
                <a href="/languages/${lang.id}/delete">Delete</a>
            </td>
        </tr>
        </c:forEach>
    </tbody>
</table>
<p><form:errors path="language.*"/></p>
<form:form action="/languages" method="post" modelAttribute="language">
    <p>
        <form:label path="name">Name</form:label>
        <form:input path="name"/>
    </p>
    <p>
        <form:label path="creator">Creator</form:label>
        <form:input  path="creator"/>
    </p>
    <p>
        <form:label path="version">Version</form:label>
        <form:input path="version"/>
    </p>
    <input type="submit" value="Submit"/>
</form:form>
</body>
</html>