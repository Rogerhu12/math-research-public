# GPR 初始完整区间算术失败及直接 Taylor 修复

[run46134446655/1](https://github.com/Rogerhu12/math-research-public/actions/runs/46134446655) 于2026-11-28 10:19:00 UTC failure，事件 `b49e0830a0ed5fbf9063e537694d2e4a8c373e0f`。完整log 74072 bytes，SHA256 `4337eb89bea3559796f46a804e45c627ea23c1077bc9139af47fc9347f912806`。实际断言是 `true negative nominal q on the entire physical cell`，不是数学上证明真实q非正。原176整输入和整个GCS私有载体身份准入均已先完成。日志未到第64格前缀，因此只有失败处在索引0–63之内的证据；没有可登记或恢复的成功GPR格，不能猜实际索引，也不能把此说成无科学调用。

原scalar producer定义 `point_jets[k]=f^(k)/k!`、`whole_final_derivative=f^(7)(I)`、`complete_true_value=f(I)`，原整626格均有独立whole q正性。修复改为直接Horner求原Taylor公式：对j阶归一化导数，先取 `binomial(7,j) f^(7)(I)/7!`，逐次乘完整有符号x并加 `binomial(k,j) point_jets[k]`。这与原精确多项式加余差式代数相同，但不调用对零中心有半径Arb球的generic幂；后者的已知运行时行为在原R97R中已记录。所有(-h)的整数幂也逐次相乘。该说明给出实现修复，不把推断触发形状等同于本次未输出的实际失败格。

零阶Taylor enclosure与同一原件的完整 `complete_true_value` 相交；先严格要求二者有限且重叠，原q whole正性及输出q严格正门均保。相交只收紧同一已准入函数的两个全格外包，不取中点、不改端点、不缩真实域。完整原次数、176自然件/626格/193方向坐标、两phase及omega和完整角圆周合同不变。

owner增加每格异常记录：实际stage、plan双有理端点、原cubic/scalar索引、真正完成格数及整段未压缩字节链SHA。完整输出和定量门仍独立，任何失败均不升级为全域成功。源及workflow pins同步后继续同一未完成新目标；GCS仅按原whole身份恢复为必要输入，旧科学结论不重授。
