# R874首次整格运行的相对域坐标接口修复

2026-11-16 08:47:03 UTC。

公开run43833749948/job133185135987，源fc6d692d2429e1e058c4c371e59b0f49ce201baf，在descend(c1)处停止，未生成整格或范数结论。原因是Sage相对数域元素的polynomial()返回内部绝对表示，不是声明的基域F上的1,ω系数。producer的descend与eval_L两处改用list()，保全部原数学公式及整性断言。

[Sage官方元素文档](https://doc.sagemath.org/html/en/reference/number_fields/sage/rings/number_field/number_field_element.html)明确说明该区别。没有删除断言或把失败当数学反例。修复提交自动触发同一公开workflow，继续实际格和映射候选。
