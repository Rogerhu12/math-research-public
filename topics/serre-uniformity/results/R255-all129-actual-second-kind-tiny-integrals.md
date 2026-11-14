# R255：全部129个有理圆盘的完整第二类小积分

日期：2026-11-13。**状态：全部129盘、每盘108维 de Rham 小积分已实算。**

本篇在 R228/R231 的同一真实有理中心及同一整参数上，完成 R240 全部54个第二类微分的小积分，精度为模 $47^4$；与原54个全纯微分合并后，每盘都有108个小积分。这里的小积分是从所存中心到盘内变量点的差，中心的大积分精度和完整 QC 截面的状态分别保留。R247 的超奇异中心第二类大积分仍仅有模 $47^3$，没有因本篇而增加一位。

## 1. 固定实际对象和参数

令 $X=X_{\rm ns}^{+}(41)$，$L=K_X+D$，$g=54$，$\deg L=126$。计算环为
$$R_4=(\mathbf Z/47^4\mathbf Z)[i]/(i^2+1).$$
使用 R228 的110个有理超奇异盘及 R231 的19个普通盘；没有有理尖点盘。这些都是完整73个射影坐标给出的真正粗模点，椭圆点也沿用原先已校准的粗模坐标。

每个已保存图使用一个 Frobenius 固定线性截面 $h$ 及坐标截面 $c$，规范为
$$W(z)h=1,\qquad z=W(z)c-W(0)c.$$
实际有理盘由 $z\in47\mathbf Z_{47}$ 参数化。置 $y=z/47$，则 $y\in\mathbf Z_{47}$。

R228/R231 已保存全部 $W,V_2,V_3$ 的0至3次系数。程序直接复用这些系数，并重新核验 $W h=1$、其正次项为零、全部坐标的实际 Frobenius 下降和两个固定截面的下降。没有用未去粗模化的椭圆族参数代替 $z$。

ProjectiveJetFrames 的实际全局导子 $H_h$ 给出
$$H_c(z)=V_3(z)H_hc.$$
每个 $H_c(0)$ 都是单位。若一个微分写成 $s/q^2\,\omega_L$，其准确 $dz$ 系数是
$$\frac{s(W(z))}{q(W(z))^2H_c(z)}.$$
这里的 $H_c$ 保留了真实 Kodaira–Spencer 尺度，并非仅取权二截面的数值。

## 2. 在全部129盘上消掉旧表达式的可去奇点

R240 的原第二类行向量记为 $\boldsymbol\nu$。R246 给出完整恒等式
$$\boldsymbol\mu=(\boldsymbol\nu+d\boldsymbol F)C,$$
其中 $C$ 为明确可逆整矩阵，$\boldsymbol\mu$ 是 Frobenius 固定的有理基。在原全局模型中
$$\boldsymbol\mu=\frac{\boldsymbol N}{w^2}\omega_L,\qquad
\boldsymbol F C=\frac{\boldsymbol A}{vw}.$$
$\boldsymbol N$ 是54个三次截面，$\boldsymbol A$ 是54个二次截面；其系数和 $v,w,C,C^{-1}$ 均来自 R246 的已发布证书。本次重新核验 $CC^{-1}=C^{-1}C=I$。

原 R240 分母在两个有理盘上不是单位：
$$\text{SS\_j0\_20},\qquad\text{SS\_j10\_06}.$$
这两个盘都不包含真正的第二类极点，不能把表达式的零分母视为微分本身有极点。

本次直接在全部129个真实中心核验
$$v(P)\in R_4^\times,\qquad w(P)\in R_4^\times.$$
因此两个分母在每个完整闭剩余盘上都是单位。R246 原先只专门核验了全部超奇异图及尖点；这里另外核验了全部19个真实普通中心，并没有把旧范围自动外推。

在每个原图中计算
$$
\boldsymbol\mu(z)=
\frac{V_3(z)\boldsymbol N}{w(W(z))^2H_c(z)},\qquad
\boldsymbol G(z)=\boldsymbol F(W(z))C
=\frac{V_2(z)\boldsymbol A}{v(W(z))w(W(z))}.
$$
$\boldsymbol G$ 求到三次，$\boldsymbol\mu$ 求到二次。于是
$$
\boxed{\boldsymbol\nu_k=
\bigl(\boldsymbol\mu_k-(k+1)\boldsymbol G_{k+1}\bigr)C^{-1},
\quad k=0,1,2.}
\tag{255.1}
$$
所有逆均是单位逆。两个可去奇点盘也使用同一个准确公式，不做非单位除法。

## 3. 与原微分表达式的独立局部核对

令 $v_{\rm old}$、$\boldsymbol s$ 为 R240 原分母及原54个三次分子。本次保留它们，另作下列核对：

1. 在原分母为单位的127个盘，直接展开
   $$\frac{V_3(z)\boldsymbol s}{v_{\rm old}(W(z))^2H_c(z)}$$
   至二次，与 (255.1) 每个系数逐项相同。共核验
   $$127\cdot54\cdot3=20574$$
   个 $R_4$ 等式。
2. 在全部129个盘，把 (255.1) 乘回原分母，核验
   $$v_{\rm old}(W(z))^2H_c(z)\boldsymbol\nu(z)
   =V_3(z)\boldsymbol s\pmod{z^3,47^4}.$$
   共核验
   $$129\cdot54\cdot3=20898$$
   个等式。对两个可去奇点，完整正规性来自第2节的全局恒等式和单位分母；这里没有仅凭交叉相乘后低阶相同就推断正规商。
3. 每个 $\boldsymbol\mu_k$ 及 $\boldsymbol G_k$ 都逐项实，即虚坐标为零。换回原第二类基后，逐项满足 R240 原极点族的 Frobenius 置换：
   $$\overline{\boldsymbol\nu_k}
     =(\boldsymbol\nu_k)_{\tau_2}.$$
   原基不逐项有理；程序没有把它的虚部擅自删掉。
4. 同时从原 $W(z)$、$H_c(z)$ 重算全部54个全纯微分
   $$\boldsymbol\omega(z)=W(z)K_1/H_c(z),$$
   并按原典范 Frobenius 矩阵核验其下降。

全部等式通过；两个旧分母可去奇点的清单也与逐盘直接检测完全相同。

## 4. 模47⁴的完整小积分和全尾界

对每个原第二类坐标，
$$
\boxed{
\int_{P_{\rm center}}^{P(y)}\nu_j
\equiv47(\nu_0)_j y
+\frac{47^2}{2}(\nu_1)_j y^2
+\frac{47^3}{3}(\nu_2)_j y^3
\pmod{47^4}.}
\tag{255.2}
$$
全纯微分采用完全相同的积分公式。结果保存了全部108个坐标的三个 $y$ 系数，不只保存一个采样点值。

完整余项控制如下。原图是整光滑参数图，$v,w,H_c$ 的常数项均为单位，所以 (255.1) 的完整未截断微分属于 $R_4[[z]]\,dz$；其特征零整提升也属于相应的整形式幂级数环。第 $n$ 次积分项的估值至少为
$$n-v_{47}(n).$$
对所有 $n\ge4$，该值都至少为4。因此整个高阶尾项在 $z\in47R_4$ 时消失模 $47^4$。这不是仅依据多项式已经截断而忽略可能的分母。

(255.2) 对每个盘的全部 $y\in\mathbf Z_{47}$ 同时成立。它本身不决定中心大积分，也不把108个积分坐标当作 Poincaré 规范截面的高度。规范截面仍须保留 R148 的代数纤维、真实主函数范数和 R140/R141 的换框。

## 5. 产物和恢复

生成器：

- scripts/p41_all129_second_kind_tiny47.py。

完整证书：

- scripts/data/p41_all129_second_kind_tiny47_complete.json.gz；
- SHA256：bdd06433d1403fcd11a6e1251a5ef2562c8acdfcb4b7ee377adc1d322e217405。

证书按原10个图保存全部129个盘、原参数和框架、$\boldsymbol\mu$ 的0至2次系数、$\boldsymbol F C$ 的0至3次系数、原 $\boldsymbol\nu$ 的0至2次系数，以及108个小积分的三个 $y$ 系数。全部源文件及固定输入的 SHA 随证书保存，原中心和高阶射影坐标从 R228/R231 的已发布完整 atlas 读取。

在课题目录重建：

~~~
OPENBLAS_NUM_THREADS=1 python scripts/p41_all129_second_kind_tiny47.py \
  --script-dir scripts \
  --output p41_all129_second_kind_tiny47_complete.json.gz
~~~

实际运算复用精确模矩阵实现；浮点矩阵通道仅在每个非负内积的整数和严格小于 $2^{53}$ 时启用，两个复坐标的实乘积先各自转回整数再取差。较大的内积自动使用原准确整数通道。

依赖：R228/R231 的完整真实有理 atlas；R234 的全部全纯小积分接口；R240 的实际54个第二类微分；R246 的已证移极点恒等式。R247 和 R248/R256 提供各自范围内的中心常数；它们的精度范围不因本篇而被改写。

本篇完成全129盘的第二类小积分。下一项实际计算继续 R254 的普通点 Hecke 支撑和主函数范数，以及 R148 规范 QC 截面的同一纤维换框；全部共同根仍未求出。
