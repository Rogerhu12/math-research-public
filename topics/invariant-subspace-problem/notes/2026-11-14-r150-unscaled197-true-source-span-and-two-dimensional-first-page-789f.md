# R150：197 个未缩放来源的实际第一进位坐标与二维相关第一页

日期：2026-11-14（UTC）。作者：Astra-ISP-789f，AI-assisted，GPT-6 Astra Pro。

本稿读取已完成的原 197 系统，证明其投影第三列实际张成整个
\((U_9)_2\)，并结合完整原来源包的形式局部源核定理，识别扩大来源包
在 \(s=2\) 的完整第一页为二维 \(s=2I\) 模。它没有重算原乘积，
没有把相关局部消去写成全局多项式来源，也没有完成原目标的后续三位提升。

## 1. 唯一小读取与原数据

实际小任务为 run43654741434 / job132630693334；
源码提交 e7d0638b1cefb8c7831006d8788bdce645c7c2c0，
数据提交 c09e0eececed0a4fb85ee82b741ef5826aa7d077。

- [实际完整坐标回执](r150-197-unscaled-selector-actions-789f/43654741434-1/unscaled197-first-carry-source-space-receipt.json)；
- [Actions 回执](r150-197-unscaled-selector-actions-789f/43654741434-1/actions-outcome.json)；
- [全量保存清单](r150-197-unscaled-selector-actions-789f/43654741434-1/complete-actual-recovery-publication-manifest.json)；
- [完整读取程序](2026-11-14-r150-unscaled197-first-carry-source-space-789f.py)。

只读取原 run43653360404 的两个 JSON 和两个矩阵系统，全部 stored/decoded
SHA 均实际核对；程序又逐块核系统 SHA、矩阵 SHA、真实基、列标签及完整坐标身份。
实际数学时间为 0.036855237 秒，限额 10 秒、512 MiB。
五份完整恢复共 256910 字节均已实际发布；其中包括四份输入和本次完整结果。
没有重新执行旧 VQ、整数乘积、jet 求解或 197 第三方向。

## 2. 同一真源基中的准确坐标

沿用 \(\mathbf F_{31}\) 上的原 315 维余模 torsion、真实 primary 投影
\(P_2\)，以及真源基
\[
 V_{10}=U_9+\mathbf F_{31}b_{10},\qquad
 b_{10}=d_{9305}.
\]
这里第十列是实际未投影来源的像；程序使用已经支付的真实基变换，
没有将 \(P_2b_{10}\) 当作 \(b_{10}\)。

令 \(D_j\) 为原 197 计算沿指定整数代表实际求出的
\[
 D_j=\frac{R_{2j}-\sum_{i=1}^7 b_i c_{ij}-Aq_{2j}}p,\qquad
 j=2,\ldots,198,
\]
在相关 primary 中的类。其十项来源、一次真实除 \(p\) 和五项投影的范围，
见[形式局部第一页定理](2026-11-14-r150-saturated-source-envelope-first-page-and-primary-choice-control-789f.md)。
本稿只读取它已经保存的 \(P_2D_j\)，不另选 \(q_2\)。

实际求得唯一 \(C\in\mathbf F_{31}^{10\times197}\) 并核
\[
 [b_1,\ldots,b_{10}]\,C=[P_2D_2,\ldots,P_2D_{198}]
 \quad\hbox{于全部315坐标}.
\tag{2.1}
\]
结果为
\[
 \operatorname{rank}[P_2D_2,\ldots,P_2D_{198}]=7,
 \qquad C_{10,j}=0\quad\hbox{对全部197列}.
\tag{2.2}
\]
完整 \(10\times197\) 系数和旧 \(7\times197\) 的
trueSevenCancellation 数组都在回执中。

由 (2.2)，全部投影列在 \(U_9\) 内；由于这些列已经是纯 2-primary，
它们在 \((U_9)_2\) 内。已付 \(\dim (U_9)_2=7\)，所以等维给
\[
 \boxed{\operatorname{span}_{\mathbf F_{31}}
       \{P_2D_2,\ldots,P_2D_{198}\}=(U_9)_2.}
\tag{2.3}
\]
因此这个投影后的列空间也在 \(s\) 下不变。
不由此断言未投影原 \(D_j\) 的 span 或其它 primary 的像。

## 3. 原来源编号与三层商的完整作用

在真 \(V_{10}/U_7\) 的坐标 \((b_8,b_9,b_{10})\) 中，原作用为
\[
 J_{10/7}=
 \begin{pmatrix}2&0&27\\0&2&0\\0&0&2\end{pmatrix}.
\tag{3.1}
\]
最先两列的实际坐标为
\[
 P_2D_2=(10,11,0),\qquad
 P_2D_3=(24,28,0)\pmod{U_7}.
\tag{3.2}
\]
它们分别是原高核 \(K_2,K_3\)，原 head 标签为 1089、1090，
不是目标列 2、3 的编号。
\[
 \det\begin{pmatrix}10&24\\11&28\end{pmatrix}
 =16\ne0\pmod{31}.
\]
完整 197 列在三层商的结果为：

| 真源商 | 常数列秩 | 完整多项式像维数 | 所选原来源 | 像上的 \(s\) 作用 |
|---|---:|---:|---|---|
| \(V_{10}/U_7\) | 2 | 2 | \(K_2,K_3\) 的投影进位 | \(2I_2\) |
| \(V_{10}/U_8\) | 1 | 1 | \(K_2\) 的投影进位 | \(2\) |
| \(V_{10}/U_9\) | 0 | 0 | 空 | 空 |

本次每个 quotient action、所有197列的坐标乘回和多项式像不变性均已实际核验。
这些是整个有限模的精确身份，不是几个 \(s\) 值的取样。

## 4. 完整原来源包的相关第一页

[完整原来源包定理](2026-11-14-r150-full-p2-source-envelope-by-197-unscaled-columns-789f.md)
给真正的全局整数矩阵
\[
 B_{\rm sat}=[A,b_1,\ldots,b_7,pb_8,p^2b_9,R_{22},\ldots,R_{2,198}],
 \qquad\operatorname{im}B_{\rm sat}=(\operatorname{im}A:p^2).
\]
其完整第一页只在已经支付的形式局部环
\(\mathbf Z_{(31)}[[t]]\)、\(t=s-2\) 中使用。
由[完整局部源核及选择差证明](2026-11-14-r150-saturated-source-envelope-first-page-and-primary-choice-control-789f.md)，
\[
 \operatorname{im}\beta_{B_{\rm sat},2}
 =\operatorname{span}_{\mathbf F_{31}[[t]]}
     \{[b_8],[P_2D_2],\ldots,[P_2D_{198}]\}
 \quad\hbox{于 }\widehat Q/\widehat U_7.
\tag{4.1}
\]
实际联合 \((b_8,D_{197})\) 的坐标基可取
\[
 [\,b_8,P_2D_2\,]
 \ \longleftrightarrow\
 \begin{pmatrix}1&10\\0&11\\0&0\end{pmatrix}.
\tag{4.2}
\]
它的作用准确为 \(2I_2\)。故
\[
 \boxed{\operatorname{im}\beta_{B_{\rm sat},2}
       =(\widehat U_9/\widehat U_7)
       \simeq(\mathbf F_{31}[[t]]/(t))^2.}
\tag{4.3}
\]
这与此前自然图中“197新像在 \(Q/V_{10}\) 为零”是不同进入位。
本次没有出现第十源方向，但 \(b_9\) 在扩大来源包的第一页已真实出现。

特别需要保留：本题没有证明全部197的全局 \([R_{2j}]\in U_7\)；
全局 \(\operatorname{coker}\bar B_{\rm sat}=Q/U_7\) 不是本稿的结论。
其它 primary 不能由这个小读取自动消去。

## 5. 下一页须保完整源核

沿局部页定理记两零列坐标为 \(\varepsilon_8,\varepsilon_9\)，
新增的197个真实消去关系为 \(\zeta_j\)。
第一页中 \(\beta(\varepsilon_8)=b_8\)、
\(\beta(\zeta_2)=10b_8+11b_9\)。
若 \(\beta(\zeta_j)=a_jb_8+b_jb_9\)，则 \(11^{-1}=17\pmod{31}\)，
\[
 \zeta_j-(a_j-15b_j)\varepsilon_8-17b_j\zeta_2
 \in\ker\beta.
\tag{5.1}
\]
对 \(j=3\) 即
\[
 \zeta_3-7\varepsilon_8-11\zeta_2\in\ker\beta.
\]
此外须保 \(t\varepsilon_8,t\zeta_2,\varepsilon_9\)，以及原
\(\ker\bar F_7\) 每个来源按其第一页 \(b_8\) 系数作的真实补偿。
先由全部这些来源生成下一页，再按真正整数核身份削减；
只取197列的常数矩阵核会漏掉两个 \(t\)-关系及旧源核部分。

后继还要重新支付连续提升的整数 carry 和所需 Taylor 精度。
本次单次十项解决定五项相关类，不意味着新二、三页可以免费连续沿用同一精度。
原目标 \(B_{\rm sat}y=h_0t_j\pmod{p^4}\)、原十七式的全局正证书、
特征零成员资格以及普通 Hilbert ISP 均仍未完成。
