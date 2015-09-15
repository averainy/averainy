#!/usr/bin/python
#coding=utf-8
import xml.dom.minidom
def get_tagname():  
    doc = xml.dom.minidom.parseString(input_xml_string)  
class msg_parse:
    def __init__(self,msg):
        self.doc = xml.dom.minidom.parseString(msg)  
    def _getData(self,tagName):
        nodes=self.doc.getElementsByTagName(tagName)
        if nodes:
            return nodes[0].childNodes[0].data
        else:
            return None
    def getFromUserName(self):
        return self._getData("FromUserName")
    def getToUserName(self):
        return self._getData("ToUserName")
    def getCreateTime(self):
        return self._getData("CreateTime")
    def getMsgType(self):
        return self._getData("MsgType")
    def getContent(self):
        return self._getData("Content")
    def getMsgId(self):
        return self._getData("MsgId")
    def getPicUrl(self):
        return self._getData("PicUrl")
    def getMediaId(self):
        return self._getData("MediaId")
    def getFormat(self):
        return self._getData("Format")
    def getMediaId(self):
        return self._getData("MediaId")
    def getThumbMediaId(self):
        return self._getData("ThumbMediaId")
    def getLocation_X(self):
        return self._getData("Location_X")
    def getLocation_Y(self):
        return self._getData("Location_Y")
    def getScale(self):
        return self._getData("Scale")
    def getLabel(self):
        return self._getData("Label")
    def getTitle(self):
        return self._getData("Title")
    def getDescription(self):
        return self._getData("Description")
    def getUrl(self):
        return self._getData("Url")
    def getEvent(self):
        return self._getData("Event")
    def getEventKey(self):
        return self._getData("EventKey")
    def getTicket(self):
        return self._getData("Ticket")

if __name__ == "__main__":
    # 文本消息
    res="""<xml>
    <ToUserName><![CDATA[toUser]]></ToUserName>
    <FromUserName><![CDATA[ffdfdromUser]]></FromUserName> 
    <CreateTime>1348831860</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[this is a test]]></Content>
    <MsgId>1234567890123456</MsgId>
    </xml>"""
    abc=msg_parse(res)
    print abc.getFromUserName()
    print abc.getToUserName()
    print abc.getCreateTime()
    print abc.getMsgType()
    print abc.getContent()
    print abc.getMsgId()
    # 图片消息
    res="""<xml>
     <ToUserName><![CDATA[toUser]]></ToUserName>
      <FromUserName><![CDATA[fromUser]]></FromUserName>
       <CreateTime>1348831860</CreateTime>
        <MsgType><![CDATA[image]]></MsgType>
         <PicUrl><![CDATA[this is a url]]></PicUrl>
          <MediaId><![CDATA[media_id]]></MediaId>
           <MsgId>1234567890123456</MsgId>
            </xml>"""
    abc=msg_parse(res)
    print abc.getPicUrl()
    print abc.getMediaId()
    # 语音消息
    res="""<xml>
    <ToUserName><![CDATA[toUser]]></ToUserName>
    <FromUserName><![CDATA[fromUser]]></FromUserName>
    <CreateTime>1357290913</CreateTime>
    <MsgType><![CDATA[voice]]></MsgType>
    <MediaId><![CDATA[media_id]]></MediaId>
    <Format><![CDATA[Format]]></Format>
    <MsgId>1234567890123456</MsgId>
    </xml>"""
    abc=msg_parse(res)
    print abc.getFormat()
    # 视频消息
    res="""<xml>
    <ToUserName><![CDATA[toUser]]></ToUserName>
    <FromUserName><![CDATA[fromUser]]></FromUserName>
    <CreateTime>1357290913</CreateTime>
    <MsgType><![CDATA[video]]></MsgType>
    <MediaId><![CDATA[media_id]]></MediaId>
    <ThumbMediaId><![CDATA[thumb_media_id]]></ThumbMediaId>
    <MsgId>1234567890123456</MsgId>
    </xml>"""
    abc=msg_parse(res)
    print abc.getThumbMediaId()
    # 地理位置消息
    res="""<xml>
    <ToUserName><![CDATA[toUser]]></ToUserName>
    <FromUserName><![CDATA[fromUser]]></FromUserName>
    <CreateTime>1351776360</CreateTime>
    <MsgType><![CDATA[location]]></MsgType>
    <Location_X>23.134521</Location_X>
    <Location_Y>113.358803</Location_Y>
    <Scale>20</Scale>
    <Label><![CDATA[位置信息]]></Label>
    <MsgId>1234567890123456</MsgId>
    </xml> """
    abc=msg_parse(res)
    print abc.getLocation_X()
    print abc.getLocation_Y()
    print abc.getScale()
    print abc.getLabel()
    # 链接消息
    res="""<xml>
    <ToUserName><![CDATA[toUser]]></ToUserName>
    <FromUserName><![CDATA[fromUser]]></FromUserName>
    <CreateTime>1351776360</CreateTime>
    <MsgType><![CDATA[link]]></MsgType>
    <Title><![CDATA[公众平台官网链接]]></Title>
    <Description><![CDATA[公众平台官网链接]]></Description>
    <Url><![CDATA[url]]></Url>
    <MsgId>1234567890123456</MsgId>
    </xml> """
    abc=msg_parse(res)
    print abc.getTitle()
    print abc.getDescription()
    print abc.getUrl()
    # 关注/取消关注事件 
    res="""<xml>
    <ToUserName><![CDATA[toUser]]></ToUserName>
    <FromUserName><![CDATA[FromUser]]></FromUserName>
    <CreateTime>123456789</CreateTime>
    <MsgType><![CDATA[event]]></MsgType>
    <Event><![CDATA[subscribe]]></Event>
    </xml>"""
    abc=msg_parse(res)
    print abc.getEvent()
    # 扫描带参数二维码事件
    # 用户未关注时，进行关注后的事件推送
    res="""<xml><ToUserName><![CDATA[toUser]]></ToUserName>
    <FromUserName><![CDATA[FromUser]]></FromUserName>
    <CreateTime>123456789</CreateTime>
    <MsgType><![CDATA[event]]></MsgType>
    <Event><![CDATA[subscribe]]></Event>
    <EventKey><![CDATA[qrscene_123123]]></EventKey>
    <Ticket><![CDATA[TICKET]]></Ticket>
    </xml>"""
    abc=msg_parse(res)
    print abc.getEventKey()
    print abc.getTicket()
    # 用户已关注时的事件推送
    res="""<xml>
    <ToUserName><![CDATA[toUser]]></ToUserName>
    <FromUserName><![CDATA[FromUser]]></FromUserName>
    <CreateTime>123456789</CreateTime>
    <MsgType><![CDATA[event]]></MsgType>
    <Event><![CDATA[SCAN]]></Event>
    <EventKey><![CDATA[SCENE_VALUE]]></EventKey>
    <Ticket><![CDATA[TICKET]]></Ticket>
    </xml>"""
    abc=msg_parse(res)
    print abc.getEventKey()
    print abc.getTicket()
    # 上报地理位置事件
