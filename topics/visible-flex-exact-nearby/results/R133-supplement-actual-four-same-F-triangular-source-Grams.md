# R133：四格同 F 三角补片与完整 128 源 Gram 的实际验证

2026-11-14，visible-exact-astra-0df9。

**状态：实际完成。** 公开 Actions run
[43648579604](https://github.com/Rogerhu12/math-research-public/actions/runs/43648579604)
的科学 child 返回 0，15 门全部通过；科学源耗时
183.47545535800003 秒，child 墙钟 185.00590222199997 秒。
本条仅授原索引 0、76、3300、5969 的局部完整矩阵数据，
没有授予全5970矩阵 Green 或无限维逆。

## 1. 同一个完整矩阵

原 run 43645186441 的四个 full193 forward F、其全部原数组与
193 维误差证书逐字节复用。原 target、原 projector validator、
原 forward F 及既成 Green 的重算次数均为 0。

本次每端保留原准确 dyadic 的96列 Q，并新选、保存97列补空间 N。
完整 $S=[Q,N]$ 的 Gram 与真逆均实际验证。相对原 forward F，只作
[完整合同](../notes/2026-11-14-R133-same-F-triangular-matrix-Green-contract.md)
(G.1)–(G.6) 的线性端点补片 $F(t)=F_0(t)+t\Delta$，使端点矩阵准确上三角。
被删除的下块完全进入 $\Delta$、微分残差与真生成元差；没有称真实生成元
本来就上三角。

下表将原 directed 证书向安全方向简写；均为上界，$\sigma$ 一列为下界。

|原格|完整 $\|\Delta\|$ 上界|$\sigma_{\min}(F)$ 下界|完整 $\|\widetilde A-A_{\rm true}\|$ 上界|完整 $\|F^{-1}-C\|$ 上界|
|---:|---:|---:|---:|---:|
|0|1.110767e−13|0.808132441002|2.100932e−8|2.063126e−13|
|76|3.222134e−9|0.169323678476|1.432758e−4|3.104790e−7|
|3300|9.971294e−12|0.992310484148|5.246524e−6|1.020105e−11|
|5969|2.598218e−12|0.921217094960|1.953006e−7|3.312833e−12|

C 是原准确 dyadic generator 的 degree24 无舍入递推多项式，
满足所验证的 $C'+CA$ 残差门。通过 $(CF)'$ 的两项估计得到真 $F^{-1}$
的包络；旧 independently rounded backward F 没有充当此真逆。

## 2. 三种单位、所有方向与真实 mean

每格实际保存三个独立 source Gram：

- cross_reference：真实物理高态97…160输入所对应的193×128交叉
  多项式提议；其准确输出位于33…96的128槽。
- edge_y_unit：加权 y 源中的单位128槽。
- edge_physical：普通物理源经真实 $R(r)$ 加权后的128槽。

交叉模型保持所有128个 primitive 中间模。原 raw 完整误差确为
Wiener/乘法算子门，最高角导从384到640的安全膨胀取5/3；
线性 $R$ 与原三次模型的完整 degree4 乘积不截掉。
新增交叉矩阵舍入另付，输入没有错误地右除高态 R。

|原格|完整交叉 source uniform 误差上界|cross_reference 的完整 H 上界迹|
|---:|---:|---:|
|0|1.295546e−8|0.006317017|
|76|7.664513e−5|0.505679224|
|3300|3.120207e−8|0.000082798215|
|5969|2.783721e−7|4.491960e−8|

H 的单位是按该格真实 dr 积分的完整 source 核平方矩阵，不是
最终 BVP 响应范数。全193行、p/q相关项和独立 even mean 保留；
signed 矩阵乘积完成后，才通过完整误差得到 Loewner 上界。
实际保存对象为对称 dyadic 中点加准确非负 diagonal slack。
原格76的 cross Gram slack 约1.366574e−7，是包络费用；
不能把它当成实际误差的下界。

输出 J 同时保留 weighted y 和 ordinary $h$ 的完整 Gram。
odd/even 分行积分后准确带入闭格 $\rho_{\min}$，mean 无非零模缩放。
原格3300确实跨越固定安全相位上端
2383968743003/10000000000000，故本次实际保存其准确负窗交段；
5969整格在负窗内；0和76的负窗输出准确为零。
没有把当前固定背景的端点免费外推到非零 δ 或未知非线性背景。

## 3. 原过程身份与公开字节

发布源的完整身份：

- source SHA256
  2173281e0558cbbabf3a21d506ae3cf9b0253a9406aa2d9d15b8681e8faeaf44。
- worker SHA256
  98ca04e2a5e0691f9e9f319d16700f8884da6eea27f3eb61eb832d3107b19f38。
- 112项 manifest SHA256
  a24a9a7fec2f39e349e9f547ea4d5c33f72db10d41e3a77ed7030409161e7ad9；
  原105项逐项不变。

公开证据根目录为：

    notes/same_F_triangular_source_Gram_pilot_ci/run-43648579604-1-same-F-triangular-source-Gram-pilot/

- native/complete-four-same-F-triangular-source-Grams.json.gz：
  24778 B，SHA256
  9a46d9fc76499a17a90a0a153a0c4907415eadcedfd9f50f70fd82d08f9dbc7c。
- process.json：12424 B，SHA256
  954d803891494df3176641dfc42275566f9eadec3c93b73c87216afaab01840f。
- evidence/complete-same-F-matrix-Gram-pilot-summary.json：
  28522 B，SHA256
  230b4ba04a7851393904a59a7dc8928db3ba06b6c5c56e4e9e360bc7a197a94a。
- evidence/complete-same-F-array-origin-inventory.json：
  15724 B，SHA256
  c074bc428fd7940cf63bbef1941eb621d3c412cf39b2a6e2bdf835eb05d5e695。

四个新的 NPZ 仅在本公开 Actions artifact 中保留：
visible-exact-same-F-matrix-Gram-pilot-43648579604-1，
artifact ID 14135471378，9996896 B。四个原 full193 数组仍在其
原 run 43645186441 的 artifact，未以本次新 origin 冒认。

原格0、76、3300、5969的新增 NPZ SHA256 依次为：

    e991ce3015b18b24a360a17052b40e8350357d08119aff80a17c0c11549d86c9
    42b135a67d4e8643dfde4f2c05ab873cc9769227025c623f4f7f232cd433ed20
    134ccde009d574f31deed8e3a066d9074f6996619b70e9a769e4171fc9f7b2fe
    26d987012bb9d7f90599a96862bb735434b0a3a2bd83bb16857c3db10a2bfdd5

原 matrix run 的 artifact process SHA 是
c0da036701912c0ccf453306e434303ce832a4971496d6f5ddcd7a9afc9392cb，
其公开 repo 科学快照为
7198cd349d5403757728ba641cbc9bf501c6bc2dc2aebafd17c81a62fd95fbdd。
实际验证逐字段确认，唯一差异是 artifact 多了 final:true 的出版
checkpoint 4a78f35f345c054563e907863c85df19141ea0a2；
其余每个字段及全部科学 native/数组相同，两份原过程均完整保留。

本次 process 记录五次真实 pull 与 README 检查，全部 diff 为空。
最后一次在22:36:06 UTC，读到
b13b2dc7cf689bc90dd61a06fde0f4a75ea5bee9。
原 source、原数学输入和全部已成数组均未改变。

## 4. 后继使用边界

这些实际矩阵可用于合同 (G.14)–(G.18) 的全方向双扫，并保留
128方向输入的径向 L²空间。四个独立局部样本不是全5970覆盖；
完整连续源缺陷、真实两端97/96行、V舍入跳及帽 high trace 仍各付。
尤其名义 $q_N=0$ 不等于完整 true-cap Robin/mean 已满足。

本条没有证明真正无限维 q_ν、负区高 BVP、全低高 Schur、
非零 δ 的完整逆或最终非线性存在。已成 finite193 真逆与新局部
矩阵的作用明确分开；后继必须消费全区实际核和全部后验负荷。
