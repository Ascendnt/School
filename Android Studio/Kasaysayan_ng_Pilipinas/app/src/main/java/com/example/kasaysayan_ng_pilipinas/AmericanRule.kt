// American Rule
package com.example.kasaysayan_ng_pilipinas

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button

class AmericanRule : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_american_rule)

        val americanVideoButton = findViewById<Button>(R.id.americanVideoButton)
        americanVideoButton.setOnClickListener{
            val Intent = Intent(this, AmericanVideo::class.java)
            startActivity(Intent)
        }

        val americanDescriptionButton = findViewById<Button>(R.id.americanDescriptionButton)
        americanDescriptionButton.setOnClickListener{
            val Intent = Intent(this, AmericanDescription::class.java)
            startActivity(Intent)
        }



    }
}