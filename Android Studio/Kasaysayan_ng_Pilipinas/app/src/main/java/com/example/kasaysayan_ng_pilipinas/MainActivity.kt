package com.example.kasaysayan_ng_pilipinas

import android.content.Intent
import android.os.Bundle
import android.view.Menu
import android.widget.Button
import androidx.navigation.ui.AppBarConfiguration
import androidx.appcompat.app.AppCompatActivity
import androidx.viewpager2.widget.ViewPager2
import com.example.kasaysayan_ng_pilipinas.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    private lateinit var appBarConfiguration: AppBarConfiguration
    private lateinit var binding: ActivityMainBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val spanishRuleButton = findViewById<Button>(R.id.spanishRuleButton)
        spanishRuleButton.setOnClickListener{
            val Intent = Intent(this, SpanishRule::class.java)
            startActivity(Intent)
        }

        val japaneseRuleButton = findViewById<Button>(R.id.japaneseRuleButton)
        japaneseRuleButton.setOnClickListener{
            val Intent = Intent(this, JapaneseRule::class.java)
            startActivity(Intent)
        }

        val americanRuleButton = findViewById<Button>(R.id.americanRuleButton)
        americanRuleButton.setOnClickListener{
            val Intent = Intent(this, AmericanRule::class.java)
            startActivity(Intent)
        }

        val philippineSelfRuleButton = findViewById<Button>(R.id.philippineSelfRuleButton)
        philippineSelfRuleButton.setOnClickListener{
            val Intent = Intent(this, PhilippineSelfRule::class.java)
            startActivity(Intent)
        }


//        val viewPager2: ViewPager2 = findViewById(R.id.viewPager2)
//        val images = listOf(R.drawable.spanishrule,R.drawable.japaneserule,R.drawable.americanrule,R.drawable.philippinesselfrule)
//
//        viewPager2.adapter = ViewPagerAdapter(images)

    }
}