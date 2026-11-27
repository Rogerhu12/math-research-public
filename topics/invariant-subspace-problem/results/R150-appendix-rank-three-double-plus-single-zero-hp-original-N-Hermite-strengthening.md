# R150：四有限源 Hp0 图的原 N 二阶系数及孤立点一阶降式

日期：2026-11-27（Asia/Taipei）。作者：Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。

**状态：本稿的原系数恒等式与必要归约已证明；参数图尚未据此判空。** 在原 rankH=3、H 型2+1、rankV=2、Hp=0、essT3=6 的四有限源图上，保留[原完整有理重建](R150-appendix-rank-three-double-plus-single-zero-hp-finite-source-rational-reconstruction.md)与[两线性七式](R150-appendix-rank-three-double-plus-single-zero-hp-two-linear-original-ideal-equivalence.md)的同一物理定位。这里补入原完整 N 极线在二重点的二阶条件，并将既有孤立点一阶条件降到 d 次数8。没有对只在解上成立的关系求导，也没有新增一般位置假设。

## 1. 原对象与确切求导

仍在已证九次域
$$
K_e=\mathbb Q[e]/(16e^9-108e^8+36e^7-15e^6+18e^4-1)
$$
中工作。令
$$
R_e=2e^3+1,\quad Q=4e^3-1,\quad D_e=2e^3+1-12e^4,
\quad b=-R_e/6.
$$
这些所需常数均是既有已付单位。物理参数为二重点 s、孤立点 w=s+d，以及两个 V 源的对称参数 x,z。沿用原核 k(s,w)、原范数
$$
n=N_s=k(s,\alpha)k(s,\beta),\quad
\Delta=x^2-4z,\quad q_p=x^3-5x^2+x^2z-6xz+32z-5z^2,
$$
$$
\beta=b_s=-2s^2(s-2)(s+6),\quad E=s^2-sx+z.
$$
本稿简写 k=k(s,w)，k'=\partial_s k，n'=\partial_s n，beta'=\partial_s beta；所有这些 s 导数均保持 **w,x,z 固定**。以 d 替代 w 后，准确导数为
$$
\partial_s\big|_{w,x,z}=\partial_s\big|_{d,x,z}-\partial_d.
\tag{1.1}
$$
令
$$
H=k n'-2nk',\qquad
\Lambda=\frac{\Delta q_p}{4e^2n},\qquad
q=\frac{2R_e nk}{3H}.
\tag{1.2}
$$
这里 q 是原 jet 比例；不要与 q_p 混同。原 jet 范数等价于
$$
P_J=3e^2H^2+2R_e\Delta q_p\beta n k^2=0.
\tag{1.3}
$$
原定位已经支付 e,beta,n,k,Delta,q_p；(1.3) 又使 H 为单位。因此本稿全部有理分母均在原商环中合法。n=E²Q_n、k=−d²Q_w、H=dE W_d 与前稿完全一致。

## 2. 从原完整 N 读取二阶系数

令 r=s+t，并记
$$
f(r)=k(s,r),\quad j(r)=\partial_s k(s,r),\quad g(r)=k(w,r).
$$
在原完整 N 中，P_* 与 S_* 在 s 都有至少二重零，所以它们的平方不贡献 t² 系数。剩余部分准确为
$$
\frac{N_r}{\Lambda n}-2\mathcal H(r)+4\mathcal J(r),
$$
$$
\mathcal H=2\Lambda f\{q(j-k'f/k)-f/4\}+\frac{g^2}{2\Lambda k^2},
\qquad
\mathcal J=b\Lambda f^2+\{q(j-k'f/k)-f/2\}\frac gk.
\tag{2.1}
$$
这些是原重建的完整极线，未删 V 项。

原核给出字面多项式身份
$$
f(s+t)=-\frac\beta2t^2+O(t^3),\quad
j(s+t)=\beta t+\frac{\beta'}4t^2+O(t^3),
$$
$$
g(s+t)=k+k't+\frac{k''}2t^2+O(t^3),\quad
N_{s+t}=n+n' t+\frac{n''}2t^2+O(t^3).
$$
代入 (2.1)，原 N 的真实二阶系数为
$$
c_2=\frac{n''}{2\Lambda n}
-\frac{(k')^2+kk''}{\Lambda k^2}
+q\beta'+6q\beta\frac{k'}k+\beta.
\tag{2.2}
$$
每个完整原解都必须满足 c2=0。

定义新的原多项式
$$
\boxed{P_2=
3e^2\{2\beta n H'-2\beta n'H-n\beta'H\}
-(8e^3+1)\Delta q_p\beta^2nk.}
\tag{2.3}
$$
它不是对 (1.3) 的求导。准确恒等式是
$$
\boxed{
\Lambda c_2=
\frac{P_2}{12e^2\beta n^2k}
+P_J\left\{
\frac{\beta'+6\beta k'/k}{12e^2H\beta nk}
+\frac1{6e^2n^2k^2}\right\}.}
\tag{2.4}
$$
验证 (2.4) 只需使用 H=kn'−2nk' 与 H'=kn''−n'k'−2nk''，展开有理函数；不使用 G9 或任何临界点关系。源另以独立符号 n,n',n'',k,k',k'',beta,beta',Delta*q_p 检查两边差严格为零。

由原单位与 (1.3)，c2=0 当且仅当 P2=0。P2 还字面被 E² 整除；源验证准确商乘回。因此可把
$$
P_2/E^2=0
\tag{2.5}
$$
加入前稿原七式，无新增定位因子。这个新生成元在 d 中次数5，完整整数展开有5694项；这里只保存生成源与哈希，不存展开数组。

## 3. 孤立点原 N 一阶系数的低次返回

原重建第6节已经证明
$$
QW(r_w-d_w)-2R_e\,\partial_s\partial_w\log k=0,
$$
其中 W=H/(2nk)、r_w=(partial_w N_w)/(2N_w)、d_w=(partial_w k)/k。此处沿用该结论，新增的是保全部原零纤维的降式。

令
$$
L_2=2A_sA_w+(A_sB_w+B_sA_w)x+2zB_sB_w,
\quad S_w=A_sB_w-B_sA_w,
$$
$$
k_w=\partial_wk,\quad
C_k=k\partial_s\partial_wk-k'k_w,
\quad H_w=k\partial_wN_w-2N_w k_w.
$$
清除原单位后，既有条件为
$$
F_w=QHH_w-8R_e nN_wC_k=0.
\tag{3.1}
$$
两个真正的**普遍恒等式**为
$$
L_2^2-4nN_w=\Delta S_w^2,
\quad
2L_2\partial_wL_2-4n\partial_wN_w=2\Delta S_w\partial_wS_w.
\tag{3.2}
$$
第二式是对第一式这一普遍多项式身份求导，不是对解集上的约束求导。

原 J、C 使 S_w=0。原未平方单点比例式是
$$
K=2e^2QL_2-D_e\Delta q_p k=0.
\tag{3.3}
$$
因此 L2 是强迫单位，Nw=L2²/(4n) 亦是单位，不需另选子图。

置
$$
M_w=QH(k\partial_wL_2-L_2k_w)-4R_e nL_2C_k,
$$
$$
\boxed{\widetilde F_w=
QH(2e^2Q\partial_wL_2-D_e\Delta q_p k_w)
-4R_eD_e n\Delta q_p C_k.}
\tag{3.4}
$$
完整的两条降式身份为
$$
4nF_w=2L_2M_w+\Delta S_w\{-2QHk\partial_wS_w
+2QHS_wk_w+8R_enS_wC_k\},
\tag{3.5}
$$
$$
2e^2QM_w=k\widetilde F_w-K(QHk_w+4R_enC_k).
\tag{3.6}
$$
源将 (3.2)、(3.3)、(3.5)、(3.6) 全部作为整数多变量恒等式实际乘回。故在原七式与同一物理定位上，Fw=0 当且仅当 tildeFw=0。最后仅约掉字面公因子 E*d；商在 d 中次数8，保所有原物理纤维。没有除任何新的首项。

## 4. 实际检查与后续单位门

[自含新源](../notes/2026-11-27-h21-original-N-Hermite-true-Ke-8542.py)继承原七式的冻结输入哈希与全部八条原恒等式，只新增本稿两个原 N 系数。`--build-only` 在本地实际 exit0，4.926643秒，验证全部新旧身份与原分母范围。新输入在 d,z,x,s 上的相应次数为 (5,8,8,24) 与 (8,9,9,21)，并完整保原 inverse 变量 nPi−1；此处 nPi 的符号 n 是旧脚本定位变量，不是正文的 Ns。

构建回执见[小回执](../notes/2026-11-27-h21-original-N-Hermite-build-8542.json)。完整数域单位门单独执行，仍只承认**特征零下原生成元与实际证书乘积等于1**。计算使用数域模方法进行带转换矩阵的尝试，先在同一数域检查一个小单位输入；若算法不可用或实际输入超时，均记录未决，不据模点或软件返回码判空。所用方法接口核对 [Singular 算法说明](https://www.singular.uni-kl.de/web/docs/examples-computing-groebner-and-standard-bases-2e3cac91.html)、[liftstd 的转换矩阵定义](https://www.singular.uni-kl.de/web/docs/reference-liftstd-4249be07.html)和[数域模方法](https://www.singular.uni-kl.de/web/lib/nfmodstd.html)。

三种旧七式900秒未决仍按原记录保留；本次是加入真实 N 系数后的加强输入，不重做旧失败，也不宣称已经取得单位证书。整个课题的完成标准不变。


## 5. 本次真实执行：仍未取得单位身份

[完整小回执](../notes/2026-11-27-h21-original-N-Hermite-bounded-execution-8542.json)记录 run `45886748045`、job `140139221544`，冻结提交 `3d10ef1404c9bfebe9c60e75187f52f611662a94`、源blob `d46cd489902c5ea5a34189a06539628eb4a8703d`。Singular 4.4.1 实际通过数域关系与 `liftstd(...,"nfmod")` 小单位输入的证书回乘，随后进入10生成元的完整原输入。生成输入1,465,449字节，SHA256 `011efc5fd3fe31050196d6550da2ee9777bad5c79d5ea2127774234ecfe3000c`。

完整单位门在900秒界实际超时；总驱动905.464231秒，峰值子进程RSS714,476KiB，source exit1。只出现field/smoke/开始实际输入标记，未出现单位回乘标记；**没有 I*C=1**。这是已执行但未决的计算，不是排空证明。证明中的原恒等式不受影响；后续换更低次的原几何输入，不重复此1.465MB计算。驱动实际pull与两README无变化的SHA记录亦在回执中。
