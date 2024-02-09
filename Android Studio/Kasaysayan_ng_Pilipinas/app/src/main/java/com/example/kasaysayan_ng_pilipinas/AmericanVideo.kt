package com.example.kasaysayan_ng_pilipinas

import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.MediaController
import android.widget.VideoView

class AmericanVideo : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_american_video)

        val americaVideoView = findViewById<VideoView>(R.id.americaVideo)
        val packageName = "android.resource://" + getPackageName() + "/" + R.raw.american
        val uri = Uri.parse(packageName)
        americaVideoView.setVideoURI(uri)

        val mediaController = MediaController(this)
        americaVideoView.setMediaController(mediaController)


    }
}