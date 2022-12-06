package com.efrei.dev2.tp3;

import android.os.Bundle;

import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentTransaction;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;

public class FormFragment extends Fragment {

    private View fragView;
    private EditText name, firstName;
    private Button sendBtn;
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        fragView = inflater.inflate(R.layout.fragment_form, container, false);
        sendBtn = (Button) fragView.findViewById(R.id.sendBtn);

        sendBtn.setOnClickListener(sendBtnClick);



        return  fragView;
    }

    private View.OnClickListener sendBtnClick = new View.OnClickListener() {
        @Override
        public void onClick(View view) {
            name = (EditText) fragView.findViewById(R.id.edName);
            firstName = (EditText) fragView.findViewById(R.id.edFirstName);

            Bundle bdl = new Bundle();

            bdl.putString("name",name.getText().toString());
            bdl.putString("firstname",firstName.getText().toString());

            DetailFragment dtFrag = new DetailFragment();
            dtFrag.setArguments(bdl);

            //FragmentManager fragManager = getActivity().getSupportFragmentManager();
            FragmentManager fragManager = getParentFragmentManager();
            FragmentTransaction fragTransaction = fragManager.beginTransaction();
            fragTransaction.replace(R.id.fLayout,dtFrag).commit();
        }
    };


}