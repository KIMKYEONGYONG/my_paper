//
//  ViewController.swift
//  JLVG_CANDO
//
//  Created by 김경용 on 2023/01/18.
//

import UIKit
import Foundation
import DropDown

class ViewController: UIViewController, HomeModelProtocol, UITextFieldDelegate, TopicHomeModelProtocol {


    var levelFeedItems: NSArray = NSArray()
    var topicFeedItems: NSArray = NSArray()
    
    var selectedLevel : LevelModel = LevelModel()
    
    
    @IBOutlet weak var levelDropView: UIView!
    @IBOutlet weak var topicDropView: UIView!
    
    @IBOutlet weak var levelInput: UITextField!
    @IBOutlet weak var topicInput: UITextField!
    @IBOutlet weak var keywordInput: UITextField!
    
    @IBOutlet weak var levelIcon: UIImageView!
    @IBOutlet weak var topicIcon: UIImageView!
    
    @IBOutlet weak var levelBtnSelect: UIButton!
    @IBOutlet weak var topicBtnSelect: UIButton!
    
    @IBOutlet weak var topicView: UIView!
    @IBOutlet weak var keywordView: UIView!
    
    var levelList : [String] = []
    var levelDiction = [String:String]()
    
    var topicList : [String] = []
    var topicDiction = [String:String]()
    
    @IBOutlet weak var testLabel: UILabel!
    
    let levelDropDown = DropDown()
    let topicDropDown = DropDown()
    
    
    var levelId:String = ""
    var topicId:String = ""
    var keyword:String = ""
    
    var levelName:String = ""
    var topicNmae:String = ""
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
         
        //self.view.backgroundColor = UIColor(patternImage: UIImage(named: "일본.png")!)
        
    
        
        self.levelInput.delegate = self
        self.topicInput.delegate = self
        
        let homeModel = HomeModel()
        homeModel.delegate = self
        homeModel.downloaditems()
        
        initUI()
        
        topicView.isHidden = true
        keywordView.isHidden = true
    

    }


    func levelItemDownloaded(items: NSArray) {
        levelFeedItems = items
        for i in levelFeedItems{
            let j: LevelModel = i as! LevelModel
            // print(j.levelName!)
            levelDiction[j.levelName!] = j.levelId!
            levelList.append(j.levelName!)
        }
        
        setLevelDropDown()
        
        self.levelInput.reloadInputViews()
    }
    
    
    func topicItemsDownloaded(items: NSArray){
        topicFeedItems = items
        topicList = []
        for i in topicFeedItems{
            let j: TopicModel = i as! TopicModel
            topicDiction[j.topicName!] = j.topicId!
            topicList.append(j.topicName!)
        }
        setTopicDropdown()
        
        self.topicInput.reloadInputViews()
        
    }
    
    // DropDown 커스텀
    func initUI(){
        
        DropDown.appearance().backgroundColor = UIColor.systemGray
        DropDown.appearance().textColor = UIColor.black // 텍스트 색상
        DropDown.appearance().selectedTextColor = UIColor.red //선택된 텍스트 색상
        DropDown.appearance().backgroundColor = UIColor.white // 팝업 배경 색상
        DropDown.appearance().selectionBackgroundColor = UIColor.lightGray // 선택된 배경 색상
        DropDown.appearance().setupCornerRadius(8)
        
        // 레벨 Dropdown 설정
        levelDropDown.dismissMode = .automatic // 팝업을 닫을 모드 설정
        levelInput.text = "선택해주세요."
        levelIcon.tintColor = UIColor.gray
        
        // 버튼을 젤 앞으로 가져오기
        self.levelDropView.bringSubviewToFront(levelBtnSelect)
        
        
        // 토픽 Dropdwon 설정
        topicDropDown.dismissMode = .automatic
        topicIcon.tintColor = UIColor.gray
        
        self.topicDropView.bringSubviewToFront(topicBtnSelect)
        
        //self.keywordInput.backgroundColor = UIColor.gray
                
    }
    
    
    func setLevelDropDown() {
    
        // dataSource로 itemList를 연결
        levelDropDown.dataSource = levelList
        
        // anchorView를 통해 UI 연결
        levelDropDown.anchorView = self.levelDropView
        
        // View를 가리지 않고 View 아래에 Item 팝업이 붙도록 설정
        levelDropDown.bottomOffset = CGPoint(x:0, y: levelDropView.bounds.height)
        
        // Item 선택시 처리
        levelDropDown.selectionAction = { [weak self] (index: Int, item: String) in
            
            self!.levelInput.text = item
            self!.levelIcon.image = UIImage(systemName: "arrowtriangle.down.fill")
            
            self!.levelId = self!.levelDiction[item]!
            self!.levelName = item
            
           // 레벨 선택시 토픽 view 설정
            self!.topicView.isHidden = false
            self!.topicInput.text = "선택해주세요."
            self!.execTopicHomeModel()
            
            self!.keywordView.isHidden = true
            self!.keywordInput.text = ""
            //print(levelId)
            
        }
        // 취소시 처리
        levelDropDown.cancelAction = { [weak self]  in
            
            self!.levelIcon.image = UIImage(systemName: "arrowtriangle.down.fill")
        }

    }
    
    func setTopicDropdown(){
        
        // dataSource로 itemList를 연결
        topicDropDown.dataSource = topicList
        
        // anchorView를 통해 UI 연결
        topicDropDown.anchorView = self.topicDropView
        
        // View를 가리지 않고 View 아래에 Item 팝업이 붙도록 설정
        topicDropDown.bottomOffset = CGPoint(x:0, y: topicDropView.bounds.height)
        
        // Item 선택시 처리
        topicDropDown.selectionAction = { [weak self] (index: Int, item: String) in
            self!.topicInput.text = item
            //print(self!.topicDiction[item] ?? "nil")
            self!.topicId = self!.topicDiction[item]!
            self!.topicNmae = item
            self!.topicIcon.image = UIImage(systemName: "arrowtriangle.down.fill")
            
            self!.keywordView.isHidden = false
            
            
        }
        // 취소시 처리
        topicDropDown.cancelAction = { [weak self]  in
            
            self!.topicIcon.image = UIImage(systemName: "arrowtriangle.down.fill")
        }

    }
    
    func execTopicHomeModel(){
        let topicHomeModel = TopicHomeModel()
        topicHomeModel.delegate = self
        topicHomeModel.downloaditems(levelId: self.levelId)
    }
   
    @IBAction func levelDropDownClicked(_ sender: Any){
        levelDropDown.show()
        self.levelIcon.image = UIImage.init(systemName: "arrowtriangle.up.fill")
        
    }
    
    
    @IBAction func topicDropDownClicked(_ sender: Any){
        
        topicDropDown.show()
        self.topicIcon.image = UIImage.init(systemName: "arrowtriangle.up.fill")
        
    }
    
    
    
    @IBAction func jlvSearch(_ sender: UIButton) {
        
        self.keyword = self.keywordInput.text!
        
    
        let jlvResultView = self.storyboard?.instantiateViewController(withIdentifier: "JlvResultViewController") as? JlvResultViewController
        
        
        jlvResultView?.levelId = self.levelId
        jlvResultView?.topicId = self.topicId
        jlvResultView?.keyword = self.keyword
        
        jlvResultView?.levelName = self.levelName
        jlvResultView?.topicName = self.topicNmae
        
        
        // 전환 애니메이션
        jlvResultView?.modalTransitionStyle = .crossDissolve
        // 화면설정
        jlvResultView?.modalPresentationStyle = .fullScreen
        
        self.present(jlvResultView!, animated: true, completion: nil)
        

    }
    
}
