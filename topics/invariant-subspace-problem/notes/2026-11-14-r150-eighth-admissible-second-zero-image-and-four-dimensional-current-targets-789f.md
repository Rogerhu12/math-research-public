# R150：η8 完整允许第二像为零、九当前初值受阻与真实四维下一目标商

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / root、normal_annihilator；AI-assisted，GPT-6 Astra Pro。

**状态：实际计算完成，全部恢复数据已推送。** 本结论保持原 \(31^2h_0\) 目标。它排除的是保持当前 \(F_9\) 初始来源模 \(31\)、同时保持原 \(p^2\) 整数格的下一位提升，不是全部原整数来源，也不是普通 ISP 的结论。

## 1. 实际执行与原对象

固定 \(p=31\)、原 primitive 17 式矩阵 \(A\)、6188 个原来源及 4367 个输出坐标。
原目标仍为
\[
 AX_j=p^2h_0t_j\pmod{p^6},\qquad j=2,\ldots,10,\qquad p^6=887503681.
\]
本次唯一新方向标签是 9101；此前的九个当前 \(X_j\)、原 p6 乘积、正常形和余式全部复用。

| 项目 | 实际记录 |
|---|---|
| 数学 run / job | 43644262244 / 132598400950 |
| 实际源提交 | 05d80c9b4e12d47275e724fe4e992e9cb0d199b6 |
| 原冻结入口提交 | 4c30342c62edfc29968d8342af18fc53515681e3 |
| 结果发布提交 | 0ab29a88a1fffc5710c2602cb2bb610a2f9efda8 |
| 数学实际时间 | 68.417425751 秒 |
| 新原 q / H5 实际费用 | 88 / 88 |
| 新相关第二像秩 | 0 |
| 相容的当前目标 | 空集 |
| 被阻的当前目标 | 2、3、4、5、6、7、8、9、10 |

完整来源、范围与次数合同见[冻结接口](2026-11-14-r150-eighth-second-interface-789f.md)和[8 文件清单](2026-11-14-r150-eighth-second-frozen-manifest-789f.json)。
实际[主回执](r150-eighth-second-actions-789f/43644262244-1/eighth-second-pipeline-receipt.json)、[Actions 结果](r150-eighth-second-actions-789f/43644262244-1/actions-outcome.json)均为已完成数据。
源码冻结、先前本地编译和本次实际数学分开记录。

调度曾有一次 CLI HTTP 403，没有启动数学；之后既有 root 发布 run43644218789 实际 pull/rebase/push，再以 HTTP 204 成功调度一次。该过程不是重算旧九来源。数学结果发布器实际读取的 main 为4885f0d3bbdb880904ded7f531672888000d5405，两 README 无差异。

## 2. 九旧余量的实际全支撑、秩和作用

本次先逐项核对已保存九余
\[
 \rho_j=(p^2h_0t_j-AX_j)/p^5\pmod p
\]
的全部 505 个自由观察和 315 个扭坐标，不重做原乘积。
令 \(J\) 为原完整 315 维作用，\(U_9\) 为此前已证的真实九维不变像。
实际 CRT 投影 \(P_{12}(J)\) 保留根 1、2 的全部主分量，重数分别为7、32；投影多项式次数314，并实际核对
\[
 P_{12}(J)^2=P_{12}(J),\qquad P_{12}(J)U_9=U_9,\qquad
 P_{12}(J)\rho_j=\rho_j\quad\text{全部九列}.
\]

记
\[
 \mathcal R=\operatorname{span}_{\mathbb F_{31}}\{J^k\rho_j:k\ge0,\ 2\le j\le10\}.
\]
完整 Krylov 计算给：
\[
 \operatorname{rank}[\rho_2,\ldots,\rho_{10}]=9,\qquad
 \dim\mathcal R=13,
\]
\[
 \operatorname{Ann}_{\min}(\mathcal R)
 =s^4+24s^3+18s^2+11s+8
 =(s-1)(s-2)^3.
\]
投到 \(Q/U_9\) 后则为
\[
 \boxed{\dim\overline{\mathcal R}=4,\qquad
       J|_{\overline{\mathcal R}}=2I,\qquad
       \operatorname{Ann}_{\min}(\overline{\mathcal R})=s-2.}
\]
这里九个商向量的列秩也恰为4。
因此
\[
 \dim(\mathcal R\cap U_9)=13-4=9=\dim U_9,
 \qquad \boxed{U_9\subseteq\mathcal R.}
\]
这给出真实的短正合列
\[
 0\longrightarrow U_9\longrightarrow\mathcal R
 \longrightarrow(\mathbb F_{31}^{\,4},\,s=2I)\longrightarrow0.
\]

四维结论是新回执中的实际全矩阵结论。此前一个共同对偶能同时检测九目标，并不说明它们张成一维；本次数据明确排除这种误读。
上述四维空间是下一步必须命中的**实际目标商**，不能据此把整个30维相关商或所有来源先任意压成四维。

## 3. 唯一新原 H5 及完整零像

实际复用的第八第一校正为
\[
 C=(28,3,24,3,25,2,23,8,0)^T.
\]
故本次保持原整数代表和全部 carry，真正构造
\[
 \bar A q=AK4_{7003}/p^4-\sum_{i=1}^{8}b_i C_i,
\]
\[
 H_5=K4_{7003}-\sum_{i=1}^{8}p^{4-e_i}\kappa_i C_i-p^4q,
 \qquad(e_1,\ldots,e_9)=(1,1,2,2,2,2,2,3,4).
\]
\(C_9=0\) 是已实读事实，未加入无来源的第九补偿。

新 q 经完整 \(GQ+\mathrm{rem}\)、VQ、原前基 DAG 和原尺度运输恢复；
q 与 H5 的实际加权费用都为88。
程序再在原整数模 p6 乘回 H5 的全部17式，对每个输出系数验证 p5 整除。
实际每列检查232133个整数输出坐标，失败数为0；
原行单位运输和全部加权界均通过，最大系数次数77。
由此得到真实
\[
 d_8=AH_5/p^5\pmod p.
\]

新列保全部505自由观察和315扭坐标。
回执的 \(\texttt{newSecondDirectionAlreadyPrimary=true}\) 实际给
\[
 P_{12}(J)d_8=d_8.
\]
在 \(Q/U_9\) 中，其 Krylov 在幂0和1的秩均为0，最小湮灭多项式为1。
所以不只是主投影零，而是
\[
 \boxed{d_8\in U_9,\qquad
        \operatorname{span}\{J^k d_8:k\ge0\}\subseteq U_9.}
\]

此处 H5 的原 p6 乘积一般不为零；主回执中的
\(\texttt{fullOriginalSeventeenEquationIdentityMod887503681=false}\)
符合计算一个非零 p5 除后像的用途，不是 p5 整除失败。
本次没有正目标，不能把“每个相容目标都验证”的空真值当作任何一个正原式证书。

## 4. 允许初值范围内的完整否定结论

[精确整数格](2026-11-14-r150-original-p2-integer-source-lattice-and-eighth-second-direction-789f.md)已经证明
\[
 \Lambda_2=\{(x,c):p^2T_9(x,c)\text{ 为原整数来源}\}
          =\{c_8\in pD[s],\ c_9\in p^2D[s]\}.
\]
保持**当前** \(F_9\) 初始来源模p后，下一位允许核为
\[
 \ker\bar A\oplus\sum_{i=1}^{8}\mathbb F_{31}[s]\eta_i;
\]
\(\eta_9\) 不在这一位的允许整数格中。

旧1632精确核、旧四个扩增方向、旧198方向的相关第二像和
\(\eta_1,\ldots,\eta_7\) 的相关第二像已有完整覆盖。
在根1/2全部主分量模 \(U_9\) 后，唯一未算方向正是 \(\eta_8\)。
本次已经把它的全多项式像算成零；旧完整第一像也已在
[run43638830039 的证明](2026-11-14-r150-ninth-first-zero-image-all-nine-current-obstructions-and-p9-family-exclusion-789f.md)
中算成零。
故全部允许修正的相关下一像仍为零。

九个当前 \(\rho_j\) 都在该相关主分量内，而且分别在 \(Q/U_9\) 非零。
因此每个都不能由上述允许修正消去。
回执保存了九个完整315坐标对偶；它们由真正商对偶与
\(P_{12}(J)\) 复合，杀掉全部 \(U_9\) 和允许相关像，对相应目标取1。
其他主分量的旧第二像没有被声称为零；投影复合和真实目标支撑使它们不能取消这里的障碍。

**准确结论：** 对九个当前原目标，保持当前 \(F_9\) 来源模31、
同时保持 \(\Lambda_2\) 的所有允许下一位修正，均不能得到原
\(AX_j=p^2h_0t_j\pmod{p^6}\)。

本条不排更低初始来源，不把自然图 \(p^2T_9\Lambda_2\) 自动认作全部原整数解，
不声称旧198的第三像为零，也不把有限精度排除外推为全部原特征零来源排除。
既有固定 \(P_9^\infty\) 九目标全部预算排除保持原已证范围。

## 5. 全部真实恢复字节与后续复用

[恢复清单](r150-eighth-second-actions-789f/43644262244-1/recovery-manifest.json)列37个原恢复文件，共16174596字节：
18个二进制、19个小文本，其中8个完整阶段 cache。
[完整发布保全清单](r150-eighth-second-actions-789f/43644262244-1/complete-actual-recovery-publication-manifest.json)
给 fallback=0。
根逐项核对恢复清单、二进制证书、小文本和发布清单的路径、原字节数与SHA，一致性缺失数为0；
发布程序还已经实际逐个验证 gzip 分片、合并和解压后的原SHA。
[发布清单](r150-eighth-second-actions-789f/43644262244-1/publication-file-manifest.json)
的62个原结果记录共7544880字节，最大存储文件2031817字节。

| 新实际恢复对象 | 原字节数 | SHA256 |
|---|---:|---|
| H5 原17来源 | 1190614 | c98dce40859383081c3091dceebf7e7eb740b26d1c9e58b49f08b3fb13c6286c |
| H5 primitive 来源 | 1190614 | ac9d7a043282d26fd10703d9895398139deb229534f132bfff939f48fca33e3b |
| 新 q primitive 来源 | 565090 | a4686b23cfada746aeb12b98163d2ef3a9ca91e790a5863afa3d2db9e26cb389 |
| prepared 完整系统（gzip） | 31665 | b5eeddbbd31e68b738da99fc303698edf9ea504a52124a333e00add9f78afa78 |
| 第二像完整系统（gzip） | 32003 | b3fe46c2f83076433a7081cc2aea48373ba797d0cebbee86d38ade7bce5b60a0 |

恢复 artifact 为14132489956，
名称 \(\texttt{isp-r150-eighth-second-recovery-43644262244-1}\)，
ZIP7836255字节，SHA256
\(\texttt{530b4bce79193ad908107e65c99d14be2a5530b6111b222666618bbc9763938b}\)。
结果 artifact14132434866、发布 artifact14132449988亦已生成。
新 q、H5、原正常形、全相关系统和每个已完成 cache 都直接复用，不再重算。

## 6. 当前继续入口

后续须改变更低的允许初始值并处理真正第三层自由；
其精确格、已有关系的真 syzygy 提升和旧198来源的覆盖必须另证。
本次把实际余目标限定为上述四维2主商，但没有免费支付进入它的来源。
普通复可分无限维 Hilbert ISP、边界 \(N=M\) 及原一般特征零来源仍未完成。
