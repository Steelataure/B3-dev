package com.efrei.dev2.tp3;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        FormFragment formFrag = new FormFragment();
        getSupportFragmentManager().beginTransaction().add(R.id.fLayout,formFrag).commit();

    }
}