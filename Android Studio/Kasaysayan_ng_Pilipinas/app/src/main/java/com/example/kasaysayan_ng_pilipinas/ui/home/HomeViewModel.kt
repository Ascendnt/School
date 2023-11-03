package com.example.kasaysayan_ng_pilipinas.ui.home

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel

class HomeViewModel : ViewModel() {

    private val _text = MutableLiveData<String>().apply {
        value = "First Section"
    }
    val text: LiveData<String> = _text
}