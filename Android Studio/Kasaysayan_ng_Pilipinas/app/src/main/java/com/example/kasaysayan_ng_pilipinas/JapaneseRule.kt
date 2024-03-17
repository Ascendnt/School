package com.example.kasaysayan_ng_pilipinas

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button

class JapaneseRule : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_japanese_rule)

        val japaneseVideoButton = findViewById<Button>(R.id.japaneseVideoButton)
        japaneseVideoButton.setOnClickListener{
            val Intent = Intent(this, JapaneseVideo::class.java)
            startActivity(Intent)
        }

        val japaneseDescriptionButton = findViewById<Button>(R.id.japaneseDescriptionButton)
        japaneseDescriptionButton.setOnClickListener{
            val Intent = Intent(this, JapaneseDescription::class.java)
            startActivity(Intent)
        }

    }
}