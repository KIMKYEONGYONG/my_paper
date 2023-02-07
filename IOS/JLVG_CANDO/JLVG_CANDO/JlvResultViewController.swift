//
//  JlvResultViewController.swift
//  JLVG_CANDO
//
//  Created by 김경용 on 2023/01/26.
//

import UIKit

class JlvResultViewController: UIViewController, UITableViewDelegate, UITableViewDataSource, JLvHomeModelProtocol {
    
    var feeditems: NSArray = NSArray()

    var levelId: String = ""
    var topicId: String = ""
    var keyword: String = ""
    
    var levelName: String = ""
    var topicName: String = ""
    
    @IBOutlet weak var titleLabel: UILabel!
    @IBOutlet weak var inputWordLabel: UILabel!
    @IBOutlet weak var resultZeroLabel: UILabel!
    
    @IBOutlet weak var jlvResult: UITableView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        
        titleLabel.text! += "(\(levelName), \(topicName))"
        
        inputWordLabel.text! += "\(keyword)"
        
        jlvResult.delegate = self
        jlvResult.dataSource = self
        
        let jlvHomeModel = JLvHomeModel()
        jlvHomeModel.delegate = self
        jlvHomeModel.downloaditems(levelId: self.levelId, topicId: self.topicId, keyword: self.keyword)
        
    }
    
    func jlvItemsDownloaded(items: NSArray) {
        feeditems = items
        self.jlvResult.reloadData()
    }
    
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return feeditems.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        
        if feeditems.count == 0{
            jlvResult.isHidden = true
        }
        
        
        let celldenfier: String = "cell"
        let myCell: UITableViewCell = tableView.dequeueReusableCell(withIdentifier: celldenfier)!
        
        let item: JLvModel = feeditems[indexPath.row] as! JLvModel
        
        myCell.textLabel!.text = item.sentence
        
        
        // cell event
 
    
        
        return myCell
        
    }
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        tableView.deselectRow(at: indexPath, animated: true)
        
        let cellData = feeditems[indexPath.row] as! JLvModel
        
        myAlert(message: cellData.sentence!)
        
    }
    
    func myAlert(message: String){
        let alert = UIAlertController(title: "선택한 문장은 다음과 같습니다. 계속 진행하시겠습니까?", message:  message, preferredStyle: .alert)
        
        
        let okAction = UIAlertAction(title: "OK", style: .default){ (action) in
            print("OK Button")
            
            let jlvCandoResultView = self.storyboard?.instantiateViewController(withIdentifier: "JLvCandoViewController") as? JLvCandoViewController
            
            jlvCandoResultView?.keyword = self.keyword
            jlvCandoResultView?.levelName = self.levelName
            jlvCandoResultView?.topicName = self.topicName
            
            
            jlvCandoResultView?.jlvSentence = message
            
            // 전환 애니메이션
            jlvCandoResultView?.modalTransitionStyle = .crossDissolve
            // 화면설정
            jlvCandoResultView?.modalPresentationStyle = .fullScreen
            
            self.present(jlvCandoResultView!, animated: true, completion: nil)
        }
        let cancelAction = UIAlertAction(title: "Cancel", style: .cancel){ (action) in
            print("Cancel Button")
        }
        
        
        alert.addAction(okAction)
        alert.addAction(cancelAction)
        
        self.present(alert, animated: true, completion: nil)
    }

}
