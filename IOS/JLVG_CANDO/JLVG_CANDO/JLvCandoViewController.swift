import UIKit

class JLvCandoViewController: UIViewController, UITableViewDelegate, UITableViewDataSource, JLvCandoHomeModelProtocol {

    
    var feeditems: NSArray = NSArray()
    
    var keyword: String = ""
    var levelName: String = ""
    var topicName: String = ""
    var jlvSentence: String = ""
    
    var resultDiction = [String:String]()

    @IBOutlet weak var titleLabel: UILabel!
    @IBOutlet weak var selectSentenceLabel: UILabel!
    
    @IBOutlet weak var jlvCandoResult: UITableView!
    
    @IBOutlet weak var wating: UIActivityIndicatorView!
    
    override func viewDidLoad() {
        super.viewDidLoad()

        titleLabel.text! += "(\(levelName), \(topicName))"
        
        selectSentenceLabel.text! += "\(jlvSentence)"
        
        jlvCandoResult.delegate = self
        jlvCandoResult.dataSource = self
        
        let jlvCandoHomeModel = JLvCandoHomeModel()
        jlvCandoHomeModel.delegate = self
        jlvCandoHomeModel.downloaditems(sentence: self.jlvSentence, keyword: self.keyword)
        
    }
    
    func jlvCandoItemsDownloaded(items: NSArray) {
        feeditems = items
        self.jlvCandoResult.reloadData()
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return feeditems.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        
        let celldenfier: String = "resultCell"
        let myCell: UITableViewCell = tableView.dequeueReusableCell(withIdentifier: celldenfier)!
        
        let item: JLvCandoModel = feeditems[indexPath.row] as! JLvCandoModel
        resultDiction[item.result!] = item.percent!
        
        myCell.textLabel!.text = item.result
        
        wating.isHidden = true
        // cell event
 
        
    
        
        return myCell
    }
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        tableView.deselectRow(at: indexPath, animated: true)
        
        let cellData = feeditems[indexPath.row] as! JLvCandoModel
        
        myAlert(result: cellData.result!, percent: cellData.percent!)
        
    }
    
    
    func myAlert(result: String, percent: String){
        let alert = UIAlertController(title: result, message:  "유사도: "+percent+"%", preferredStyle: .alert)
        
        
        let okAction = UIAlertAction(title: "OK", style: .default){ (action) in
            print("OK Button")
        }
            
    
        alert.addAction(okAction)
        
        
        self.present(alert, animated: true, completion: nil)
    }

    
}
