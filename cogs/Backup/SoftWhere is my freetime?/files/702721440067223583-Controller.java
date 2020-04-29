package com.example.demo;

import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.sql.*;
import java.util.HashMap;
import java.util.Iterator;

@RestController
public class Controller {

    @RequestMapping(value = "/UserSuperType/getUsers", method = RequestMethod.POST)
    public String getUsers(@RequestBody HashMap<String, String> params) {
        String whereClause = buildWhereClause(params);
        try {
            ResultSet resultSet = executeQuery(String.format("SELECT \"Username\", \"PasswordHash\", \"FirstName\", \"LastName\" FROM public.\"UserSuperType\" %1$s;", whereClause));
           if (resultSet != null)
            return getResults(resultSet);
        } catch (Exception e) {
            return String.format("There was an error: %s1: %s2",e.getClass().getName(), e.getMessage()) ;
        }
        return String.format("There was no records with the specified criteria: %1$s",whereClause);
    }


    private Connection connect() {
        Connection c = null;
        try {
            Class.forName("org.postgresql.Driver");
            c = DriverManager
                    .getConnection("jdbc:postgresql://localhost:5432/postgres",
                            "postgres", "Manafest1");
            System.out.println("Opened database successfully");
        } catch (Exception e) {
            System.out.println(e.getClass().getName() + ": " + e.getMessage());
        }
        return c;
    }

    private ResultSet executeQuery(String sql) throws SQLException {
        Connection connection = connect();
        Statement stmt;
        try {
            stmt = connection.createStatement();
            return stmt.executeQuery(sql);
        } catch (Exception e) {
            System.out.println(e.getClass().getName() + ": " + e.getMessage());
        } finally {
            connection.close();
        }
        return null;
    }

    private String getResults(ResultSet resultSet) throws SQLException {
        StringBuilder results = new StringBuilder();

        fillMetaData(resultSet, results);
        fillData(resultSet, results);

        return results.toString();
    }

    private void fillMetaData(ResultSet resultSet, StringBuilder results) throws SQLException {
        ResultSetMetaData metaData = resultSet.getMetaData();
        for (int i = 0; i < metaData.getColumnCount(); i++) {
            results.append(String.format("%-40s ",metaData.getColumnName(i+1)));
        }
        results.append('\n');
    }

    private void fillData(ResultSet resultSet, StringBuilder results) throws SQLException {
        ResultSetMetaData metaData = resultSet.getMetaData();
        while (resultSet.next()) {
            for (int i = 0; i < metaData.getColumnCount(); i++) {
                results.append(String.format("%-40s ",resultSet.getString(i+1)));
            }
            results.append('\n');
        }
    }

    private String buildWhereClause(HashMap<String, String> params){
        StringBuilder whereClause = new StringBuilder("WHERE ");
        Iterator<String> itr = params.keySet().iterator();
        for (int i = 0; i < params.keySet().size(); i++) {
            String key = itr.next();
            whereClause.append(String.format("\"%1$s\"='%2$s'", key, params.get(key)));
            if (itr.hasNext()){
                whereClause.append(", ");
            }
        }
        return whereClause.toString();
    }
}

