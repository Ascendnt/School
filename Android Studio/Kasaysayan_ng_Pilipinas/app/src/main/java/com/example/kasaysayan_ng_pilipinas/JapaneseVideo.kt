package com.example.kasaysayan_ng_pilipinas

import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.MediaController
import android.widget.VideoView

class JapaneseVideo : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_japanese_video)

        val japaneseVideoView = findViewById<VideoView>(R.id.japaneseVideo)
        val packageName = "android.resource://" + getPackageName() + "/" + R.raw.japanese
        val uri = Uri.parse(packageName)
        japaneseVideoView.setVideoURI(uri)

        val mediaController = MediaController(this)
        japaneseVideoView.setMediaController(mediaController)
    }
}