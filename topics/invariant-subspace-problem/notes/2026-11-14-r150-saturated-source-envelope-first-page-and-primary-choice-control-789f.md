# 完整原 p² 来源包在 2-primary 的第一页：真实消去关系与选择范围

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit；AI-assisted，GPT-6 Astra Pro。

状态：本稿证明完整来源包在 **\(s=2\) 的原形式局部环** 中的第一页
精确归约。它不运行新的数学计算，也不把相关 primary 的第二像宣布为
全部全局第二像。完整原 \(p^2\) 来源 envelope 是全局定理；
本稿对其下一页的本题应用严格限于已计算的 2-primary。

本稿替换未发布草稿 87ae10f5dd3cc1ae83baa158ab0a4d930687f3ae。
旧稿把相关 \([R_{2j}]\in U_7\) 错写为全局结论，因而不应引用旧稿的
全局 \(q_2\)、余核或第一页结论。下面全部应用均改正这一量词。

依赖：
[原 p² 来源饱和与有限列包](2026-11-14-r150-original-p2-source-saturation-and-finite-column-envelope-789f.md)、
[197 个未缩放真来源的完整覆盖](2026-11-14-r150-full-p2-source-envelope-by-197-unscaled-columns-789f.md)、
[原第三相关像的双 jet 与 Smith 损失](2026-11-14-r150-third-bockstein-double-jet-smith-loss-and-local-source-789f.md)。

## 1. 全局来源与本稿使用的原形式局部环

令 \(p=31\)、\(\mathscr D=\mathbb Z_{(p)}[s]\)、\(R=\mathbb F_p[s]\)。
原矩阵为
\[
 A:\mathscr D^{6188}\longrightarrow\mathscr D^{4367}.
\]
横线表示模 \(p\)。真实来源满足
\[
 A\kappa_i=p^{e_i}b_i,\qquad
 (e_1,\ldots,e_9)=(1,1,2,2,2,2,2,3,4).
\]
\(b_i,\kappa_i\) 始终是已保存的原整数列，不以同余核中的任意代表替代。

对 \(j=2,\ldots,198\)，沿原真实第一消去取
\[
 \widetilde\kappa_j=\widehat K_j-p\widehat q_{1j},
 \qquad R_{2j}=A\widetilde\kappa_j/p^2.
\]
这些是真正 **未乘 \(p^2\)** 的旧零页来源。定义全局整数矩阵
\[
 F_7=[A,b_1,\ldots,b_7],\qquad
 \mathcal F_{\mathrm{sat}}
 =[F_7,pb_8,p^2b_9,R_{22},\ldots,R_{2,198}].
 \tag{1.1}
\]
前稿的全局定理是
\[
 \operatorname{im}_{\mathscr D}\mathcal F_{\mathrm{sat}}
       =(\operatorname{im}_{\mathscr D}A:p^2).
 \tag{1.2}
\]
本稿不改变它。

现在令 \(t=s-2\)，将所有原多项式按 \(s=2+t\) 代入
\[
 \widehat{\mathscr D}_2=\mathbb Z_{(p)}[[t]],
 \qquad \widehat R_2=\mathbb F_p[[t]].
 \tag{1.3}
\]
这是保 \(p\) 的形式原环：可以逐系数取整数代表和除一个已知整除的
\(p\)，没有先把 \(p\) 逆掉。也不把 \(t\) 逆掉。
以下 \(A,F_7,\mathcal F_{\mathrm{sat}}\) 仍是同一实际矩阵在 (1.3)
上的基变换；不是新选的 jet 矩阵。

置
\[
 \widehat Q=\operatorname{coker}_{\widehat R_2}\bar A,\qquad
 \widehat U_7=\langle[\bar b_1],\ldots,[\bar b_7]\rangle_{\widehat R_2},
 \qquad
 \widehat Q_7=\widehat Q/\widehat U_7.
 \tag{1.4}
\]
\(\widehat Q\) 的有限 torsion 部分就是原真实 2-primary；
其它有限 primary 在此成为零。任何形式自由部分仍须保留，
不能因取了局部环就删除它。

本题本轮使用的已付输入严格是相关版本：
\[
 [\bar R_{2j}]\in\widehat U_7\quad(j=2,\ldots,198),
 \tag{1.5}
\]
\[
 \operatorname{im}\beta_{F_7,2}
       \subseteq\langle[\bar b_8]\rangle_{\widehat R_2}
       \subset\widehat Q_7.
 \tag{1.6}
\]
(1.5) 使用旧相关第二像及既有完整自由条件，不是“十个系数吻合”
自动推出的全局像结论。(1.6) 使用原完整核的已付相关第一页：
\(\ker\bar A\) 的第一页像在 \(\widehat U_7\)，七条新增真实关系只贡献
\(b_8\)。本稿不需要把 (1.6) 升格为一个新的全局实算结论。

## 2. 形式原环中的第一页与真实 \(q_2\) 关系

对 (1.3) 上的整数矩阵 \(F\)，定义
\[
 \beta_{F,2}:\ker_{\widehat R_2}\bar F
                \longrightarrow\operatorname{coker}_{\widehat R_2}\bar F,
 \qquad
 \beta_{F,2}(z)=\left[\frac{F\widehat z}{p}\bmod p\right].
 \tag{2.1}
\]
因为 \(\bar Fz=0\)，分子逐系数可被 \(p\) 整除。
改变 lift 为 \(\widehat z+p v\) 只增加 \(\bar Fv\)，故映射定义良好，
并对 \(\widehat R_2\) 线性。

由 (1.5)，存在形式系数
\[
 c_j\in\widehat R_2^7,\qquad
 q_{2j}\in\widehat R_2^{6188}
\]
使
\[
 \bar R_{2j}=\bar A q_{2j}
                    +\sum_{i=1}^7\bar b_i(c_j)_i.
 \tag{2.2}
\]
取指定的逐 \(t\)-系数整数代表，定义形式整数列
\[
 D_j=
 \frac{R_{2j}-A\widehat q_{2j}
                  -\sum_{i=1}^7b_i\widehat{(c_j)_i}}p.
 \tag{2.3}
\]
这里仅断言完整形式解存在，没有断言本次已经有全局多项式 \(q_2\)，
更没有由 (2.2) 证明其它 primary 的消去。

按 (1.1) 的列顺序置
\[
 \zeta_j=(-q_{2j},-c_j,0,0,e_j).
 \tag{2.4}
\]
最后 \(e_j\) 是 197 个新增列的第 \(j\) 个坐标。准确有
\[
 \bar{\mathcal F}_{\mathrm{sat}}\zeta_j=0,\qquad
 \beta_{\mathcal F_{\mathrm{sat}},2}(\zeta_j)
            =[\bar D_j]\in\widehat Q_7.
 \tag{2.5}
\]
(2.3) 保原 \(b_i\)、完整形式 \(q_2\) 和整数代表 carry，
而不是只在余核中任取一个有相同投影的列。

## 3. 全部局部源核与第一页像

由 (1.5)，在本稿的局部环上
\[
 \operatorname{im}\bar{\mathcal F}_{\mathrm{sat}}
       =\operatorname{im}\bar F_7,\qquad
 \operatorname{coker}\bar{\mathcal F}_{\mathrm{sat}}
       =\widehat Q_7.
 \tag{3.1}
\]
(3.1) **不在这里声明为全局 \(R\)-模等式**。

令 \(\varepsilon_8,\varepsilon_9\) 分别为 \(pb_8,p^2b_9\) 两列的单位坐标。
全部形式源核准确由
\[
 \boxed{
 \ker_{\widehat R_2}\bar{\mathcal F}_{\mathrm{sat}}
 =\iota(\ker_{\widehat R_2}\bar F_7)
  +\widehat R_2\varepsilon_8+\widehat R_2\varepsilon_9
  +\sum_{j=2}^{198}\widehat R_2\zeta_j
 }
 \tag{3.2}
\]
生成。证明：对任何核向量，先减去匹配其最后 197 个坐标的
\(\zeta_j\) 组合，再减去两个零列坐标。余下全部坐标在 \(F_7\) 中，
必属 \(\ker\bar F_7\)。反向包含由每个关系的定义成立。
这不要求 (2.4) 自由独立，也不用像维数替代完整源核。

真实零列的一页是
\[
 \beta_{\mathcal F_{\mathrm{sat}},2}(\varepsilon_8)
       =[\bar b_8],\qquad
 \beta_{\mathcal F_{\mathrm{sat}},2}(\varepsilon_9)=0.
 \tag{3.3}
\]
结合 (1.6)、(2.5)、(3.2)，得到本稿的本题结论
\[
 \boxed{
 \operatorname{im}\beta_{\mathcal F_{\mathrm{sat}},2}
 =\left\langle[\bar b_8],
                [\bar D_2],\ldots,[\bar D_{198}]
         \right\rangle_{\widehat R_2}
 \quad\hbox{于 }\widehat Q_7.
 }
 \tag{3.4}
\]
有限相关模上同样可以保留其真实 \(s\)-作用，
以原 \(\mathbb F_p[s]\)-Krylov 生成这些列；这与 (3.4) 等价。

## 4. 形式消去与整数代表的选择差

取另一组完整形式解 \(q'_{2j},c'_j\)。
两解之差
\[
 (-q'_{2j}+q_{2j},-c'_j+c_j)
                    \in\ker_{\widehat R_2}\bar F_7.
\]
代回 (2.3)，各整数代表差中的整 \(p\) 倍只贡献
\(\operatorname{im}\bar F_7\)。故
\[
 [\bar D'_j]-[\bar D_j]\in\operatorname{im}\beta_{F_7,2}
               \subseteq\langle[\bar b_8]\rangle_{\widehat R_2}.
 \tag{4.1}
\]
所以各个 \(D_j\) 类可能改变，(3.4) 的完整生成像不变。

若 \(c_j\) 固定而仅改 \(q_{2j}\)，差属于 \(\ker\bar A\)；
其第一页像已进入 \(\widehat U_7\)。此时
\[
 [\bar D'_j]=[\bar D_j]\quad\hbox{于 }\widehat Q_7.
 \tag{4.2}
\]
若同时改了 \(c_j\)，则必须保 (4.1) 的 \(b_8\) 方向。

本稿未对 (2.3) 再做 \(b_8,b_9\) 或 \(F_9\) 消去。
若另一个实现添加了这种归一，必须记录并加回真实 carry 后才可比较。

## 5. 本次十 jet 计算为何足以读取这个相关像

本次 197 列实际采用
\[
 T_j=R_{2j}-\sum_{i=1}^7b_i(c_j)_i,\qquad
 D_j=(T_j-Aq_{2j})/p
 \tag{5.1}
\]
的前五个 \(t\)-系数。
\(c_j\) 是 prep 中真实
\(\mathrm{trueSevenCancellation}\) 的 \(7\times197\) 数组；
原 \(b_1,\ldots,b_7\) 按模 \(p^2=961\) 的十项实际乘回。
\(R_2\) 来自旧完整 \(q_1\) 的原多项式 \(V/\mathrm{DAG}\) 及 canonical-\(t\)
来源运输。\(q_2\) 由十项 unit-Schur 求解和同一真实 \(V/\mathrm{DAG}\)
回填，在完整 \(4367\times197\times10\) 输出上核验模 \(p\) 恒等。
本次没有 \(F_9\) 的额外归一。

这些是现有实际输入的准确规范，不是本稿新增的运行。
一次除 \(p\) 必须使用以上原整数列，不能拿模 \(p\) 的结果任意 lift。

旧双 jet 定理给相关 Smith 损失至多五。
若 \(q_N\) 是任意十项解，选一个 (2.2) 的完整形式解 \(q\)，则
\[
 q_N-q=k+t^5v,\qquad k\in\ker_{\widehat R_2}\bar A.
 \tag{5.2}
\]
\(t^5v\) 不改变所保留的前五项；\(k\) 在一次除 \(p\) 后的选择差
是 \(\beta_{A,2}(k)\)，已进入 \(\widehat U_7\)。
若七列表示也改变，则只再增加 (4.1) 的 \(b_8\) 类。

因此这些有限记录通过 **原真实 primary 投影和真实 \(s\)-作用**
准确给出 (3.4)。它们不构成一个新的全局多项式 \(q_2\) 身份，
也不识别其它 primary 的第二像。形式自由条件仍依旧稿的完整证明，
不能因 torsion 模只需五项就自动删除自由行。

## 6. 可独立使用的条件性全局代数引理

对任意 \(\mathscr D\) 上的 \(F_7,R_{2j}\)，如果另外已经证明
\[
 [\bar R_{2j}]\in U_7\ \hbox{于全部全局 }Q
 \quad\hbox{及}\quad
 \operatorname{im}\beta_{F_7}\subseteq\langle[\bar b_8]\rangle
                  \ \hbox{于全部全局 }Q/U_7,
 \tag{6.1}
\]
则 §§2–4 可直接将 \(\widehat R_2\) 换成 \(R\)，得到全局核生成与全局
第一页等式。这只是带明确额外假设的代数引理。

**本题没有在本稿满足或使用 (6.1) 的第一条。**
旧 197 的相关第二像不是全局 315 维第二像。
全局 envelope (1.2) 不依赖 (6.1)，两件事不能互换。

## 7. 后继的准确边界

旧自然 \(F_9/\Lambda_2\) 图的完整 197 加五第三相关像在
\(Q/V_{10}\) 为零，并给当前九目标的自然图全初值负结论。
这不使 (3.4) 为零：新未缩放来源包把同一 \(D_j\) 放在第一页，
而相关 \(V_{10}/U_7\) 可保留非零方向。

下一实际小 selector 应读取现成 \(D_j\) 在真实相关 \(V_{10}/U_7\)
中的列、\(b_8\) 及 \(s\)-作用。下一页来源随后必须由这个完整
第一页映射的核构造，不能只根据像维数挑选若干初值。

完整原 \(p^2\) 来源包虽已覆盖，\(\mathcal F_{\mathrm{sat}}\) 对原目标
模 \(p^4\) 的 membership 尚未完成；本稿的相关第一页也不表示其它
primary 已检查。普通 ISP 和原 \(N=M\) 仍为 OPEN。
