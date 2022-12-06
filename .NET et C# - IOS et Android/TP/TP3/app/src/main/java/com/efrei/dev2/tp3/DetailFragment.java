package com.efrei.dev2.tp3;

import android.os.Bundle;

import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentTransaction;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;


public class DetailFragment extends Fragment {

    private View fragView;
    private TextView tvName, tvFirstName;
    private Button backBtn;
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        fragView = inflater.inflate(R.layout.fragment_detail, container, false);
        tvName = (TextView) fragView.findViewById(R.id.NameValue);
        tvFirstName = (TextView) fragView.findViewById(R.id.firstNameValue);
        backBtn = (Button) fragView.findViewById(R.id.backBtn);

        Bundle bdl = this.getArguments();

        tvName.setText(bdl.getString("name"));
        tvFirstName.setText(bdl.getString("firstname"));

        backBtn.setOnClickListener(backBtnListener);

        return fragView;
    }

    private View.OnClickListener backBtnListener = new View.OnClickListener() {
        @Override
        public void onClick(View view) {
            FormFragment formFrag = new FormFragment();
            FragmentManager fragManager = getActivity().getSupportFragmentManager();
            FragmentTransaction fragTranscation = fragManager.beginTransaction();
            fragTranscation.replace(R.id.fLayout, formFrag).commit();
        }
    };
}