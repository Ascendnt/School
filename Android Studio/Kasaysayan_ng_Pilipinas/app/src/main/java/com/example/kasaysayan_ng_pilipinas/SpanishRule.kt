package com.example.kasaysayan_ng_pilipinas

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button

class SpanishRule : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_spanish_rule)

        val spanishDescriptionButton = findViewById<Button>(R.id.spanishDescriptionButton)
        spanishDescriptionButton.setOnClickListener{
            val Intent = Intent(this, SpanishDescription::class.java)
            startActivity(Intent)
        }

        val spanishVideoButton = findViewById<Button>(R.id.spanishVideoButton)
        spanishVideoButton.setOnClickListener{
            val Intent = Intent(this, SpanishVideo::class.java)
            startActivity(Intent)
        }
    }
}