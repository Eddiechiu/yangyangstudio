function pageScroll(){
    //�����ݹ���ָ��������������һ�����������ҹ��������������ڶ������������¹�������������
    window.scrollBy(0,-100);
    //��ʱ�ݹ���ã�ģ���������Ч��
    var delay = setTimeout('pageScroll()',10);
    //��ȡscrollTopֵ��������DTD�ı�׼��ҳȡdocument.documentElement.scrollTop������ȡdocument.body.scrollTop����Ϊ����ֻ��һ������Ч����һ���ͺ�Ϊ0������ȡ��ֵ���Եõ���ҳ��������scrollTopֵ
    var sTop=document.documentElement.scrollTop+document.body.scrollTop;
    //�жϵ�ҳ�浽�ﶥ����ȡ����ʱ���루����ҳ��������������޷��������������ҳ�棩
    if(sTop==0) clearTimeout(delay);
}