# R133 补篇：真实共同参考根点的完整 signed 第一强迫

2026-11-15，visible-exact / phase_inverse。

**状态：公开 Actions 的新根点代数已完成，11门全部通过。**
采用同一共同径向势和实际 nonradial fold，在先作准确 signed 消去后，
完整归一化第一强迫的角均值模小于 $6\,10^{-5}$。
在零宽 old-circle Wiener 范数下，第一行小于0.936、第二行小于0.265；
三个原角条带和前三阶角导均有完整输出界。

本篇限原真实根、固定 intrinsic $\eta_0$ 和同一修补显式族。
它没有把根点界提升为整片源范数，没有求解新的 $w_1^V$，
也没有关闭独立物理 even mean、完整 old-circle remainder 或全高逆。

## A. 实际运行和保留的第一次失败

新实际运行是
[43692226895/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43692226895)。
workflow event 与实际科学 checkout 同为
c7ff35e0ccc7c754942590c8c20af99efed8ebd2。
科学子进程退出0，实际数学时间
0.3784299789999963秒，父进程记录的子进程 wall time
0.7653538379999958秒。

原第一次运行
[43691675493/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43691675493)
的失败身份完整保留。它通过9个入口门、逐字读取3个旧阶段，
但在复矩形分母的模下界检查处以 child1 停止，
没有完成一个新的强迫 case。其实际数学时间为0.360076374秒。

该分母本身在原域中非零。对全部 $1\le l\le96$，
$$
 \Re(1-l^2z)\ge1-\frac{96^2}{97^2}
                =\frac{193}{9409}>0.
 \tag{A.1}
$$
修复仅把同一复球的下界读取从 abs(den).lower() 改为
den.real.lower()。这是完整模长的合法下界，没有扩大原参数域或放松非零门。
其余11件输入和原 worker 逐字不变。
本次重新执行了第一次未完成且按规则销去的临时代数；
没有重新计算任何旧成功 target、FFT、intrinsic、fold、repair 或 Taylor 系数。

原失败小结论仍在
[第一次 actual-result](../notes/genuine_reference_signed_root_forcing_ci/run-43691675493-1/actual-result.md)
和
[第一次 execution](../notes/genuine_reference_signed_root_forcing_ci/run-43691675493-1/execution.json)。
其 SHA256 分别为
f3f75785aa98323d67cf7e01eec0b4a46044706379a357a5b275e888aba2c92f
和
a8fc52edac163539fd8fb474c2803c05b3af9f29c852b9755f3639ce6677db24。

## B. 精确对象和所算的 signed 表达式

使用
[已证明的完整 signed 第一强迫恒等式](R133-supplement-signed-first-forcing-and-root-cancellation-for-genuine-common-reference.md)，
尤其(F.20)--(F.22)。实际覆盖
$$
 |\Re\delta|,|\Im\delta|\le10^{-8},\qquad
 |\Re z|,|\Im z|\le\frac1{9409}.
 \tag{A.2}
$$
对真实输入取 $z=j^{-2}$，全部 $|j|\ge97$、两个
$\epsilon=\operatorname{sgn}j$ 和物理频率 $n=4|j|$ 被同一计算覆盖。
原完整65中心、193方向及两个修补均值全部保留；复参数乘积为bilinear，
不是共轭乘积。

令 $C=d_\phi|_*$、$D=\partial_r-d\partial_\phi$，
并沿原(F.16)记 $L,q_\infty,\kappa_*$。本次确实组装
$$
 \begin{split}
 f_b^V(0,\phi)={}&V_j(0)-V_\infty(0)
 -\kappa_*^{-2}\left[
 \left(\frac{12L}{35}-\frac32q_\infty\right)C
 -\frac{291}{140}C^2+\frac{15}{14}DC
 +2bK_rP(v^2)\right],\\
 f_a^V(0,\phi)={}&\frac{i\epsilon}{\kappa_*}
                   \left(\frac85C_\phi-\vartheta_*\right).
 \end{split}
 \tag{A.3}
$$
特别保留 $2bK_rP(v^2)$，没有先代 $K=0$ 再错误删除其导数。
$DC$ 的角均值准确等于 $\langle C^2\rangle$，因此
$$
 \langle f_b^V\rangle
 =V_j(0)-V_\infty(0)
           +\frac{141}{140\kappa_*^2}\langle C^2\rangle .
 \tag{A.4}
$$
这不是两个势上界相减；有限频差使用(F.22)的完整提因式表达式，
在固定 $z$ 下作真实径向导数。$z=0$ 是频率极限，不是独立物理 even mean。

原多项式乘积以完整卷积组装，输出范围 $[-384,384]$ 全保。
角导的实际倍率为 $4il$。每个系数先在完整复参数盒上取统一模上界，
再作完整 Fourier 加权和；没有把逐参数范数 supremum 错换成 joint 系数和，
也没有把输出投回背景的96阶。

## C. 根点均值与全频分母的实际界

以下便读值均从原返回上界向上圆整：
$$
 \begin{split}
 |\langle f_b^V\rangle|&<5.999083248299\,10^{-5}<6\,10^{-5},\\
 \left|\frac{141}{140\kappa_*^2}\langle C^2\rangle\right|
       &<3.617128874112\,10^{-5},\\
 |V_j(0)-V_\infty(0)|&<2.868829287195\,10^{-5},\\
 |(V_j(0)-V_\infty(0))/z|&<0.190814674367 .
 \end{split}
 \tag{A.5}
$$
最后一行使用在 $z=0$ 可去的完整因子，包含该点。
这些是完整复族的上界，不是某个实参数样本的误差下界。

原实际分母门给
$$
 |1-l^2z|>0.020512271672,\qquad
 |1+z\alpha/\eta|>0.999998245388 .
 \tag{A.6}
$$
(A.1)仍是第一门的准确解析依据。幅度角均值(A.4)的微小性不关闭独立物理均值方程。

## D. 全 old-circle 输出和前三角导

记 $\|\cdot\|_{\mathcal A_\sigma}$ 为按完整物理Fourier标签加权的
Wiener范数。下表给
$\|\partial_\phi^q f_b^V(0,\cdot)\|_{\mathcal A_\sigma}$ 的向上圆整界。

| $\sigma$ | $q=0$ | $q=1$ | $q=2$ | $q=3$ |
|---|---:|---:|---:|---:|
| $0$ |0.935646|4.238392|21.506752|130.728889|
| $1/128$ |0.969425|4.410485|22.559463|138.868856|
| $3/128$ |1.041184|4.780644|24.868555|157.174036|

完整非constant第一行也独立保存。其零阶界在上述三个条带分别小于
0.935586、0.969365、1.041124；正阶角导与全第一行的对应界相同。
这里只从已成同一 signed 多项式准确取出均值，没有用两个上界的差产生新界。

第二行
$\|\partial_\phi^q f_a^V(0,\cdot)\|_{\mathcal A_\sigma}$ 为：

| $\sigma$ | $q=0$ | $q=1$ | $q=2$ | $q=3$ |
|---|---:|---:|---:|---:|
| $0$ |0.264232|2.203046|19.195120|178.029782|
| $1/128$ |0.282043|2.358588|20.642818|192.802601|
| $3/128$ |0.321544|2.705984|23.912142|226.709268|

两个carrier之间的准确规则为
$$
 f_{b,-}^V=f_{b,+}^V,\qquad f_{a,-}^V=-f_{a,+}^V
 \tag{A.7}
$$
且使用同一个复 $\delta$，不引入共轭。
两行分别保留，未把两个 Wiener 上界的平方和误称完整向量 Wiener 范数。

## E. 原输入复用和实际执行身份

科学入口是
[fourfold_codazzi_genuine_reference_signed_root_forcing.py](../scripts/fourfold_codazzi_genuine_reference_signed_root_forcing.py)，
24947 bytes，SHA256
869238d3824927a929b171d6830223d2723864f23149726444afc555b1e7e4d8。
[12件输入及全部参数](../notes/2026-11-15-R133-genuine-reference-signed-root-forcing-CI-inputs.json)
为6861 bytes，SHA256
4b72d34bb7b4d24195aa135255697a25173bcfb92ff7275e6d8b34c2ffd03597。
公开worker为17371 bytes，SHA256
fca0aacd7a4c1504f0d0fb9dcec7cd01eb2f2da9c0167542d54dc56b363102ff；
workflow为.github/workflows/visible-exact-genuine-reference-signed-root-forcing.yml，
SHA256 8d678ae075aebeacc5118f098c1af61513212d9f4bff1c7fa6b36b57bfcded27。

CLI为--repo、--manifest、--manifest-sha、--out-dir。
Python3.12.14、python-flint0.9.0、NumPy2.3.5、SciPy1.17.0和320-bit Arb
均与声明一致。12件输入实际为7件固定历史blob、3件当前相同旧字节和2件当前新文本。
完整输入收据SHA256为
722397b248758dfb16e1758041604cb06a98c29c84c6e826e7127baa2c649630。
历史输入固定在a3d84d905ce72e3a854874bbe98d119623f3f8de。

唯一读取的三个旧自然阶段是：

| 原stage | bytes | SHA256 |
|---|---:|---|
| complete-background-root-series |75245|a6f89d9bf9523d04fd0534f7224b7a8bb3ecc8b0b201ffccf3839585df56b0c8|
| complete-local-operator-series |198895|2361459d324b9de0cfe2d53e06ad5f168d91110e72ac920c28fdc779e2fd87f2|
| leading-complete-Q |80521|0aa0da3c5260ebab0f64afaf0df07eab854988a9a630260714a783ef1c21d523|

三者保持原source e4ccbf4b…、原manifest226e5aca…、原runtime、
原payload和publication身份，没有改标成新运行的阶段。
新的数学只有(A.3)--(A.5)的完整signed根点代数及其输出范数。

runner于07:57:50.969474 UTC和07:57:58.933224 UTC
真实pull，前后均是上述c7ff35e0…科学提交；
两次根README及课题README实际diff均为空。
3件immutable Python完整AST检查实际通过。
11门包括原75stage保留的完整Taylor运行身份、真实根/参数、
三个旧stage逐字身份、两修补均值、完整signed均值和全部Fourier输出，
以及两carrier/old primitive/独立物理mean范围。

## F. 小结论、完整历史和后继范围

实际小结论：
[actual-result.md](../notes/genuine_reference_signed_root_forcing_ci/run-43692226895-1/actual-result.md)，
6450 bytes，SHA256
66f02392f3cbbceac4523d7fe336cc74fbc145493ab9c8bc6355f496ad41a90e。

实际执行身份：
[execution.json](../notes/genuine_reference_signed_root_forcing_ci/run-43692226895-1/execution.json)，
23306 bytes，SHA256
4abbe1fff48c2ced17e60dd94e855858757788d3d1c8164025c187f3f53ccc40。

原科学process只在runner临时目录，11967 bytes，SHA256
160a5f8d0c2465fd3addf3e0450eed30ecbcb335a107d79a2172e85cc0f3edd2；
完整临时native为37876 bytes，SHA256
47d8341bd48dedd8061ba7ca71fc7b49e5e63fe4e7fbf15dd905d469502f084f。
按当前rule15，没有新数据、artifact或Release上传。
上述小execution已保留必要最终均值、完整范数、真实门和过程身份。

实际结果支持继续对同一rootpiece作准确signed势复合与新的第一幅度修正。
整片分析必须使用真正的共同坐标逆像，不能把$V(T_{\rm actual})$
换成同物理$r$的径向值。原第一修正不能直接改名，
原物理接缝、全部old-circle $P/I/J$ 项、独立even mean、
正区两个端口及未知高频反馈仍须分别支付。
