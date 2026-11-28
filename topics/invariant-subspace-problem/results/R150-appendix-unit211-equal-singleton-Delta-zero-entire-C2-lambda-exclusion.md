# R150：碰撞Delta零的整个二次lambda因子原纤维排除

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。

**结论。** h=k、Delta=0原图中的整个
$$C_2(\lambda)=\lambda^2-\lambda+\tfrac13=0$$
纤维为空。此为附加 C2 条件下的整纤维排除；旧七 lambda 全覆盖已经撤回，不能推断整个 Delta 零支只余 C4。新的正确剩余范围见[三个小因子及4788界](R150-appendix-unit211-h-equals-k-corrected-small-factor-exclusions-and-4788-points.md)。Delta非零图独立保留。

## 1. 使用全部原相容覆盖

此前[完整C2原相容定理](R150-appendix-unit211-equal-singleton-C2-Delta-zero-complete-original-quartic-cover.md)已经给出整个
$$\Psi(u)=133u^4-30u^3-32u^2-24u+16=0,$$
并准确恢复
$$\lambda=-\frac{133u^2-132u+20}{234u-108},$$
$$Q=3+3\lambda+(\tfrac52-15\lambda)u+(-\tfrac{11}2+12\lambda)u^2.$$
原分母234u-108在完整相容纤维上非零；其与133u²-132u+20的QQ Bézout也由新源实际返回。

本次对Psi的完整QQ因式分解及全部乘积作精确返回：Psi是一个四次不可约因子，重数1；与导数gcd为1。不是选择其中一个实根或近似根。

令
$$K=\mathbb Q[u]/(\Psi).$$
全四维常数代数中的同一点可写为
$$\lambda=\frac74+\frac29u-\frac{17}{12}u^2-\frac{1729}{288}u^3,$$
$$Q=\frac{17}{12}-\frac{25}{6}u+\frac{103}{12}u^2+\frac{133}{96}u^3.$$
程序逐式核C2(lambda)=0、原二次u式、原Delta和两个原相容式。所有四个K嵌入均保留。

## 2. 完整原Gram及同一自由参数

原物理单位A、B、lambda、u、u-1、u-ell、ell、P02、T0、J-Q、u+Q-1、Q、1-Q、bc、Phi、Pf、S在K中逐个核为非零。每个用到的逆都来自QQ[u]上的xgcd并乘回，因此不存在未付范数逆。

取r²=1-Q，
$$b=\ell/2+(u-\ell)r/(2(1-Q)),\quad c=\ell-b.$$
仍保留整个自由f，原P1严格恢复
$$t=-(P_c+P_ff)/(bcQ\Phi).$$
原另一仿射条件在同一个f,t上恒为零。原值V的前三矩、E0、N0、P1、NV及两个单点同一h=k目标全部逐式返回。

随后从原双点乘法、原单位向量(1,0,1,1)、迹和Gram算子实际构造八条原条件
$$E1,EBe,EBo,N1,NBe,NBo,PBe,PBo.$$
对f的次数依次2,2,2,2,3,3,3,3。共轭的偶奇系数对应两个真正单点；r非零使原两行同时为零必使偶奇部分分别为零。

这里K的维数是4，lambda自身仍满足原二次C2。日志一个沿用模板的lambdaDegree字段写4，指本次u常数域维数；实际恢复关系与全部恒等式如上，不将lambda误认作四次参数。

## 3. 完整原单位身份

在K[f]上，原E1与EBe的精确扩展Euclid返回
$$a(f)E1(f)+b(f)EBe(f)=1.$$
完整乘积逐个系数核验，所得最终f多项式确为1。全部八原行、实际同lambda/u/Q、两个原标签的可再生证书共3564字节。当前仅保原源、定义及小回执，不另存可重算系数载荷。

此身份在K的每个复嵌入下仍成立，对所有复f均成立。因此该四次u覆盖没有任何原Gram解；也就排除了整个C2(lambda)原纤维。没有借模因式或数值取样提升结论。

## 4. 真实执行和材料

源：
[2026-11-27-unit211-equal-singleton-complete-C2-finite-original-Gram-8542.py](../notes/2026-11-27-unit211-equal-singleton-complete-C2-finite-original-Gram-8542.py)。

源SHA256：
74cfb3839c05301c57f8dbcaaf304181f0fa10e5a5ac806eb1cac1dced8618b5。

实际run46031135735/job140614937541；驱动0.138608538秒、源0.062943102秒、最大子进程RSS37736KiB、exit0。34个常数逆及4个完整多项式除法返回。原证书SHA256：
962374d31af27b3f334ef81e429f376c9384662cc6f8afecf6b2c4413701ebd6。

stdout6490字节，SHA256：
df64efc24789d90d173ff1384184de4613a63827472376afea8423d83de81fca。

执行前真实pull读到f9d79e20c153170acab210858ce9564472b2cc1c，时间2026-11-27 16:09:25.498830 UTC，两README未变。完整原578投影和此前Q图证明门均未重放。

本页只保整个 C2 条件排除；当前正确 Delta 零覆盖仍留 F99/F300。普通Hilbert ISP尚未完成。
