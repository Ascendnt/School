package com.example.kasaysayan_ng_pilipinas

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button

class PhilippineSelfRule : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_philippine_self_rule)

        val philippineSelfRuleVideoButton = findViewById<Button>(R.id.philippineSelfRuleVideoButton)
        philippineSelfRuleVideoButton.setOnClickListener{
            val Intent = Intent(this, PhilippineSelfRuleVideo::class.java)
            startActivity(Intent)
        }

        val philippineSelfRuleDescriptionButton = findViewById<Button>(R.id.philippineSelfRuleDescriptionButton)
        philippineSelfRuleDescriptionButton.setOnClickListener{
            val Intent = Intent(this, PhilippineSelfRuleDescription::class.java)
            startActivity(Intent)
        }

    }
}