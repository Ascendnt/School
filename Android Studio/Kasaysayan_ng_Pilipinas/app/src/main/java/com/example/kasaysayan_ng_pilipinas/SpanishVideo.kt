package com.example.kasaysayan_ng_pilipinas

import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.MediaController
import android.widget.VideoView

class SpanishVideo : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_spanish_video)

        val spanishVideoView = findViewById<VideoView>(R.id.spanishVideo)
        val packageName = "android.resource://" + getPackageName() + "/" + R.raw.spanish
        val uri = Uri.parse(packageName)
        spanishVideoView.setVideoURI(uri)

        val mediaController = MediaController(this)
        spanishVideoView.setMediaController(mediaController)
    }
}