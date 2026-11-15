# R133 续篇：整片2549的真实共同参考势、首修正与完整 Taylor 尾实际结论

2026-11-15，visible-exact / phase_inverse。

**状态：公开 Actions 实际成功；仅授完整幅度和 forcing 范数，不授完整新 source norm 或全高频边值逆。**

本篇消费 [整片 signed-reference Taylor 合同](R133-supplement-whole-root-piece-signed-reference-potential-and-first-correction-Taylor.md) 的首次公开执行。[Run43694458725/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43694458725) 在部署 commit 014c5f3e5e1d5b5631cdf06b65c92401504228f5 上运行，API 为 completed/success，科学 child 为0，九个门全部通过。科学时间为7.215183343000007秒，父进程记录该 child 的 wall 时间为7.884225221999998秒。

## 1. 不可变身份和真实执行

原始小结论为 [actual-result.md](../notes/whole_root_signed_reference_Taylor_ci/run-43694458725-1/actual-result.md)，19999字节，Git blob 6033ea1e2c7ecce334f3a9f4aecbaa698985f9a6，SHA256：

67fadf7784ea30409d11a370f9e3bac63f6c1591b0b6a91213c8419bd41fa4f8。

完整小执行收据为 [execution.json](../notes/whole_root_signed_reference_Taylor_ci/run-43694458725-1/execution.json)，39214字节，Git blob f6036e9c727a4066a8e6cdd9c52380a475e6c41e，SHA256：

777e681b85beb3317853d05d1c39a35703133a7cd49c81286571d21a89fa5dd1。

科学程序为 [fourfold_codazzi_whole_root_signed_reference_Taylor.py](../scripts/fourfold_codazzi_whole_root_signed_reference_Taylor.py)，SHA256 a0f12f84d55c4735507e71e40d35cd343777d00dad4b5ec5c2e73804230198be；[67件固定输入清单](../notes/2026-11-15-R133-whole-root-signed-reference-Taylor-CI-inputs.json) 的 SHA256 为11e993bae75adf3a667ba7f7d8c28f9fb38f3fde8d12e34df938c82baef2ea65。worker SHA256 为599ce272ecd4b54ab8d7e1e40eb7d783e48f847d5b990cb7806b1d997c2c4786，workflow SHA256 为59bbdecbf34bfaeb78092dbee5e4c79a27dbd2195cbb8075ca56b23f13ad0bd3。

实际运行使用 Python3.12.14、python-flint0.9.0、NumPy2.3.5、SciPy1.17.0和320bit Arb。完整 argv 见 execution：固定 immutable science目录、manifest及上述完整 manifest SHA、临时 out-dir。67个输入全部核 bytes/SHA，原始输入来自明确历史 commit a3d84d905ce72e3a854874bbe98d119623f3f8de 或同字节当前文件；新增证明、势程序和势实际收据使用当前固定版本。完整 Python 三文件闭包实际 AST 门通过。

两次真实 pull 及两 README 的实际 diff：

| UTC 时间 | pull 后 commit | README diff |
|---|---|---|
| 08:26:18.532759 | fcd2d08eabff2ff986cdbeb5f709f11b319e537f | 空 |
| 08:26:45.619788 | 0ae6b67c1bcacf41d761effb47f7c85ab8955b3c | 空 |

同一 runner 仅启动一次科学 child。完整临时 native 为1729937字节，SHA256 675453a825f1ad09e6b496676f4c2f139f083bf96bfc34e999c9ba240a272c7c；它没有进入 Git、Release或新数据 artifact。原临时 process 为33919字节，SHA256 f1c729cd3896e17616fba6bc6e7514853f835fb035149e5e31fb50480dea0199，其科学小结完整收录于 execution。原数组和 supporting algebra 仅在临时目录内使用。

## 2. 真实对象和整片覆盖

固定原 intrinsic 参数 $\eta_0$，原 repaired65态背景和完整193方向、全复 $\delta$ 方盒半宽 $10^{-8}$ 均不改变。原根区间为
$$
 \left[\frac{1191984371497}{5000000000000},
       \frac{2383968743003}{10000000000000}\right].
$$
本次覆盖整个原物理 piece2549：
$$
 \left[\frac{2147184947341121}{9007199254740992},
       \frac{4295308144604611}{18014398509481984}\right].
$$
相对所有允许根位置的最坏旧 $\rho$ 半径为
$$
 h_*=\frac{893368603925465506687}
           {21990232555520000000000000}<41\cdot10^{-6}.
 \tag{W.1}
$$
这同时涵盖根的两侧和原不确定根带，没有把一侧长度代替双侧真实覆盖。

共同参考新增复合半径是 $R_s=3/40000$，外旧角条带为 $1/128$。原势实际结论给共同 $T$ 反像半径严格大于 $8.0060665372259\cdot10^{-5}$，所以完整 $R_s$ 域门通过。原幅度余项半径 $R_0=1/6000$ 与新增项半径 $R_s$ 分开使用，没有互相更名。

频率范围为全部 $|j|\ge97$、$n=4|j|$、两载波符号。完整复 $z=j^{-2}$ 方盒半宽 $1/9409$、所有 Fourier 输出和 amplitude mean保留。96个中间模分母统一严格下界大于0.02051227，实际有向值见 execution。这里的 amplitude mean不代替独立物理 even mean方程。

## 3. 确切新增运算及零旧重算

实际原字节消费54个完整 Taylor 阶段及两个已成阶段：完整原 holomorphic majorants 和未改变的 $f_a$ Fourier 系数范数。54阶段收据摘要 SHA256 为8b8b64fe32fd8eb75423e99edeb33be45744845f58c4b9dfb3df40cd2e82237b。两标量阶段 SHA256 分别为29ee1093b7644143c693283f774294c176a7f0989b42c004d384a856d5be5144和0a06b46b740e721742965002eced73e49b51be36abbf285a21f38c2e9efdef5a。

新建的是 degree0至12的 signed 势复合、同一真实首修正的精确积分增量、三个宽度的完整范数结论。原 target、FFT、intrinsic导数、cubic、repair、leading fold、已存 Taylor 系数和旧归一化 transport 均未重算；旧阶段字节未改写，原 $f_a$ 系数范数未再次计算。

新增关系准确为
$$
 \sigma=\bar T^{-1}(T),\qquad V_{\rm actual}=v\circ\sigma,
 \qquad f_a^V=f_a,\quad f_b^V=f_b+V_{\rm actual}.
 \tag{W.2}
$$
$\bar T=-\rho\bar A^{2/3}$ 已带旧 $\rho$ 的正确反向号。固定 $z$ 的 $r$ 导仍是 $-\partial_\rho$；复合不另乘 Jacobian。

同一完整 scalar Fuchsian积分
$$
 \mathcal B(T)=\frac12\int_0^1s^{-1/2}V(sT)\,ds,\qquad
 2T\mathcal B'(T)+\mathcal B(T)=V(T)
$$
准确保留 $\mathcal B(0)=V(0)$。新首修正由
$$
 \binom{a_1^V}{b_1^V}
 =\binom{a_1}{b_1}+
   \binom{T b_0}{a_0}\mathcal B(T_{\rm actual})            \tag{W.3}
$$
定义，未重新解旧 transport，也未将旧 $w_1$ 直接改名。实际完整 $T$ 导数上界为
$$
 |\mathcal B|<275.196107,\qquad
 |\mathcal B'|<8810.179810,\qquad
 |\mathcal B''|<766191.153907.                            \tag{W.4}
$$
它们使用同一星形复 $T$ 盘上准确质量 $1,1/3,1/5$。

## 4. 三个实际完整导数窗

下表从原有向球向外放宽。每个数是整个物理 piece、全允许复参数及输入频率的 joint Wiener 上界。径向导数是旧 $\rho$ 导绝对范数，$r$ 导绝对范数相同。表中压缩展示 angular order0，原 actual-result保全部 angular order0至3。

| 旧角输出宽度 | 场 | 值上界 | 一径导上界 | 二径导上界 |
|---|---|---:|---:|---:|
| $0$ | $f_a$ | 0.280094 | 65.141776 | 211995 |
| $0$ | $f_b^V$ | 14.228337 | 4637582 | $1.525441\cdot10^{12}$ |
| $0$ | $a_1^V$ | $2.495771\cdot10^{-5}$ | 0.757297 | 46698 |
| $0$ | $b_1^V$ | 14.600552 | 4769639 | $1.568934\cdot10^{12}$ |
| $1/1024$ | $f_a$ | 0.280094 | 65.238261 | 241336 |
| $1/1024$ | $f_b^V$ | 16.130015 | 5299964 | $1.743327\cdot10^{12}$ |
| $1/1024$ | $a_1^V$ | $2.522473\cdot10^{-5}$ | 0.784142 | 53361 |
| $1/1024$ | $b_1^V$ | 16.556297 | 5450907 | $1.793033\cdot10^{12}$ |
| $1/512$ | $f_a$ | 0.280094 | 65.366909 | 280458 |
| $1/512$ | $f_b^V$ | 18.664254 | 6183157 | $2.033848\cdot10^{12}$ |
| $1/512$ | $a_1^V$ | $2.551574\cdot10^{-5}$ | 0.818331 | 62245 |
| $1/512$ | $b_1^V$ | 19.162636 | 6359279 | $2.091837\cdot10^{12}$ |

实角处 $a_1^V$ 三角导上界小于5.901234，但其二径三角混合导上界仍小于 $5.868646\cdot10^{11}$；$b_1^V$ 相应最高混合导上界小于 $1.974015\cdot10^{19}$。这些是完整上包络，不是实际误差下界，也不证明该量级不可改善。

完整 amplitude mean的径向三行独立保存，向外压缩为：

| 场 | mean值 | mean一径导 | mean二径导 |
|---|---:|---:|---:|
| $f_a$ | 0.280092 | 64.476835 | 9785.153 |
| $f_b^V$ | 0.207723 | 72453.927 | $2.383307\cdot10^{10}$ |
| $a_1^V$ | $7.315319\cdot10^{-9}$ | 0.002396550 | 728.748 |
| $b_1^V$ | 0.213625 | 74519.299 | $2.451259\cdot10^{10}$ |

这些 mean不乘 Fourier 绝对系数和的额外条带因子，也未删除。两符号通过同一复参数的代数奇偶关系读取，未引入复共轭。

## 5. 已付完整尾与尚不能作的比较

首遗漏 degree是13。原完整 holomorphic modulus保留为
$$
 M_{f_a}<2.269413,\quad M_{f_b}<1449.591457,\quad
 M_{a_1}<0.515181,\quad M_{b_1}<1410.835060.
$$
新增项的完整 modulus是
$$
 M_{\Delta f_a}=0,\quad M_{\Delta f_b}<275.196107,\quad
 M_{\Delta a_1}<2.046438\cdot10^{-9},\quad
 M_{\Delta b_1}<283.043802.                               \tag{W.5}
$$
仅 $\Delta a_1=T b_0\mathcal B$ 使用已证三阶径向零点的 Schwarz 因子；其他项不据此缩放。每个径向系数和每个 Fourier 输出先执行同一有序 signed addition再取模。旧尾在 $R_0$、新增尾在 $R_s$ 分别作完整双 Cauchy求和，严格正角宽损进入全部角导和 mean。

根点的小 forcing已提升为真实整片的完整幅度结论，但现有二径导包络仍很大。此次公开小结保存了完整 modulus、半径和总导数界，没有保存临时数组中有限部分与两尾的逐项分拆。**本篇不从总数推定某一尾项的实际占比，也不把两个上界相减当作新相关误差证书。**

若需判定或收紧主导尾，须消费这里已公开的完整标量结论，或证明同一完整复域上的相关 remainder；所有新增标量运算仍在公开 Actions执行。单独缩小根点常数、将 $R_s$ 换成 $R_0$、删除未保存高阶系数，均不是本次结论的推论。

## 6. 九个实际门与后继接口

九门为：源/证明/manifest身份；全部历史输入字节；54阶段原 headers/payload；旧28系谱中的两完整 majorant/norm；共同 $T$ 反像覆盖；原 leading零点；scalar Fuchsian根常数及双分支；三窗 signed有限和与两完整尾；完整旧圈 remainder/mean/source/seam保留。全部为 true，failure为 null。

后继仍须对同一真实参考两列支付完整 local numerator、$H_V^{-1}$ 有序重构、旧圆周 $I/J$ 非局部项、独立物理 even mean、普通双 source端口及真实 seam跳。不能由本篇幅度表默认为真列在复角域的全算子范数已经给出；原真实列 actual 的实轴量词仍有效。

本篇只授 piece2549的 (W.2)--(W.5)及完整导数窗。相邻物理片的原 trial、非零 entry、forcing跳和积分常数保持其原身份，没有被自动替换成新参考。全 source强范数、$N97$ 高频 BVP逆、完整 low/high Schur和最终几何问题均未在本次执行中关闭。
