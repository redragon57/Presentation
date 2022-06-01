using System;
using Godot;
using T3.helpers;
using T3.resources.ECS;
using T3.resources.ECS.components;

public class Score : Control
{
    public VBoxContainer _labelStat;
    public Button _scoreBtn;
    public Label _scoreBtnTxt;
    public RichTextLabel textStats;
    public String defaultSatiTextt;
    public String defaultScoreText;
    // Declare member variables here. Examples:
    // private int a = 2;
    // private string b = "text";

    // Called when the node enters the scene tree for the first time.
    public override void _Ready()
    {
        _scoreBtnTxt = GetNode<Label>("Panel/Score/Label");
        _scoreBtn = GetNode<Button>("Panel/Score");
        textStats = GetNode<RichTextLabel>("Panel/Statistiques/Lstats");
        _labelStat = GetNode<VBoxContainer>("Panel/Statistiques");
        _scoreBtn.Connect("pressed", this, nameof(on_Score_Pressed));
        defaultScoreText = _scoreBtnTxt.Text;
        defaultSatiTextt = textStats.Text;
    }

    public void on_Score_Pressed()
    {
        if (_labelStat.IsVisibleInTree())
            _labelStat.Hide();
        else
            _labelStat.Show();
    }

    public void Update(StatisticsSystem sT)
    {
        _scoreBtnTxt.Text = Helpers.ReplaceVars(defaultScoreText, "score",
            Math.Floor(sT._statsDictionnaire[BuildingStats.Stats.Score]).ToString());
        textStats.Text = Helpers.ReplaceVars(defaultSatiTextt, "sati",
            Math.Floor(sT._statsDictionnaire[BuildingStats.Stats.Satisfaction]).ToString());
        textStats.Text = Helpers.ReplaceVars(textStats.Text, "satiJ",
            Math.Floor(sT._statsDictionnaire[BuildingStats.Stats.SatisfactionJ]).ToString());
        textStats.Text = Helpers.ReplaceVars(textStats.Text, "satiA",
            Math.Floor(sT._statsDictionnaire[BuildingStats.Stats.SatisfactionA]).ToString());
        textStats.Text = Helpers.ReplaceVars(textStats.Text, "satiV",
            Math.Floor(sT._statsDictionnaire[BuildingStats.Stats.SatisfactionV]).ToString());
        textStats.Text = Helpers.ReplaceVars(textStats.Text, "polu",
            Math.Floor(sT._statsDictionnaire[BuildingStats.Stats.Pollution]).ToString());
        textStats.Text = Helpers.ReplaceVars(textStats.Text, "sante",
            Math.Floor(sT._statsDictionnaire[BuildingStats.Stats.Sante]).ToString());
        textStats.Text = Helpers.ReplaceVars(textStats.Text, "qv",
            Math.Floor(sT._statsDictionnaire[BuildingStats.Stats.QualiteDeVie]).ToString());
        textStats.Text = Helpers.ReplaceVars(textStats.Text, "proprete",
            Math.Floor(sT._statsDictionnaire[BuildingStats.Stats.Proprete]).ToString());
    }


//  // Called every frame. 'delta' is the elapsed time since the previous frame.
//  public override void _Process(float delta)
//  {
//      
//  }
}