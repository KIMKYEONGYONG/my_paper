//
//  JLvHomeModel.swift
//  JLVG_CANDO
//
//  Created by 김경용 on 2023/01/31.
//

import UIKit

protocol JLvHomeModelProtocol: AnyObject{
    func jlvItemsDownloaded(items: NSArray)
}


class JLvHomeModel: NSObject {
    
    weak var delegate: JLvHomeModelProtocol!
    
    var data = Data()
    
    let urlPath: String = "https://jbit.bufs.ac.kr/~rlaruddyd1/jlv/IOS/jlv_search.php"
    
    
    func downloaditems(levelId: String, topicId: String, keyword: String) {
        
        let password = "72ak378D"
        var dataString = "?secretWord=\(password)"
        dataString += "&levelId=\(levelId)&topicId=\(topicId)&keyword=\(keyword)"
        let urlStr = urlPath + dataString
        print(urlStr)
        guard let encodeStr = urlStr.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed) else { return}
        
        let url:URL = URL(string: encodeStr)!
        
        
        let defalutSession = Foundation.URLSession(configuration: URLSessionConfiguration.default)
        
        
        let task = defalutSession.dataTask(with: url){ (data, response, error) in
            if error != nil {
                print("Failed to download data")
            }else{
                print("JLV Data downloaded")
                self.parseJSON(data!)
            }
            
        }
        
        task.resume()
        
    }
    
    func parseJSON(_ data:Data){
        var jsonResult = NSArray()
        
        do {
            jsonResult = try JSONSerialization.jsonObject(with: data, options: JSONSerialization.ReadingOptions.allowFragments) as! NSArray
        } catch let error as NSError {
            print(error)
            return
        }
        
        var jsonElement = NSDictionary()
        let jlvs = NSMutableArray()
        
        for i in 0..<jsonResult.count{
            jsonElement = jsonResult[i] as! NSDictionary
            
            let jlv = JLvModel()
            
            if let sentence = jsonElement["sentence"] as? String {
                jlv.sentence = sentence
                
            }
            
            jlvs.add(jlv)
            
        }
        
        DispatchQueue.main.async(execute: { ()->Void in
            
            self.delegate.jlvItemsDownloaded(items: jlvs)
            
        })
        
    }
    
}
