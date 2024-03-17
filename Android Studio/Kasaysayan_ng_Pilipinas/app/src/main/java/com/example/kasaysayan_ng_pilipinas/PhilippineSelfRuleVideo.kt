package com.example.kasaysayan_ng_pilipinas

import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.MediaController
import android.widget.VideoView

class PhilippineSelfRuleVideo : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_philippine_self_rule_video)

        val philippineVideoView = findViewById<VideoView>(R.id.philippineVideo)
        val packageName = "android.resource://" + getPackageName() + "/" + R.raw.pilipinas
        val uri = Uri.parse(packageName)
        philippineVideoView.setVideoURI(uri)

        val mediaController = MediaController(this)
        philippineVideoView.setMediaController(mediaController)
    }
}