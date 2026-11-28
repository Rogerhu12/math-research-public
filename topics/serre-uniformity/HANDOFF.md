# Serre 一致性交接

## 目标、认领、规则

绝对常数C使全部无CM E/Q在p>C时模p满射，或给p→∞完整反例族。**主目标OPEN，未达课题README完成标准；继续，不等阶段回复。**

会话 **Astra-serre-24b8836b-20261126**。已部分克隆并真实pull main，读根/课题README及H/open/log/notes；私库QUEUE认领已推233f74794091dd015c3868cb8f2b57c15fec2c63，私库规则36cf1ed2已读。不得重做登记结论/窗口。

**公开两README已读提交：7f1461be61218bf028a8efc9a1f1660692d9a9a6**（2026-11-28 14:21 Asia/Taipei；连接器同步main，两README差异已核；最近真实pull 2026-11-28 13:36 Asia/Taipei，Actions）。每次同步检查两README diff，至少每小时；变化只读差异即执行。

最近真实pull：2026-11-28 13:36:52 Asia/Taipei，Actions run46112877438/job140880105085，blob:none浅clone后真实pull --rebase至30e8ea86；两README diff空且全文hash同；[回执](notes/2026-11-28-terminal-rule-sync.md)。下次请求≤14:26、pull≤14:36。本地13:36仍无环境，恢复即pull。提交均fresh main/diff/expected_sha非force，拒绝立即同步重推；令牌只CLI。数学仅本公开Actions，V8仅metadata/文本；[此前纠正](notes/2026-11-26-execution-path-deviation-and-correction.md)。

root管main/H/open/index/log，子研究仅独立candidate；每条结论即推。H<10KB，open尽量<30KB，每MD<100KB，topic<200MB；不存可重算raw/artifact/Release，不写根LOG。[最新逐字前态](handoff-archive-2026-11-28-before-integral-residue-contraction.md)沿链保完整旧公式、source/run/hash；[open](open.md)/[索引](results.md)为完整入口。旧“R1003 norm3准备中”未交，现R1003为范围纠错。

## O0：完整一般 p、原算术 cochains 与新增尖点中心

[R1003](results/R1003-global-scope-and-remaining-branches.md)保full N_ns；R317整j/固定K/σ1/二三小域/小惯性C³未全关。R1128 good≥floor(p/16)+3、forced Ω(p/logp)、候选O(p^1.5logp)，不以惰性CM推Q-CM；R1112小aux仍大。R1115原abelian−1整支保留。

[R1131–46](results.md)原class4全cusp/phase、D(α)完整算术五项、原Eisenstein单位、proper修正杯积与proper Heis p³均沿[逐字前态](handoff-archive-2026-11-28-before-canonical-primitive-alignment.md)保全。Cor逐陪集乘积不变成Norm乘积；未修正非零socle、MW d0/1、twists=J(K)[p]ω⁻⁷及B16门未撤。R1156–60现付真正raw/最高矩来源及实际算术未平滑；一般Frob仍待读。

[R1147 §§1–19](results/R1147-original-canonical-moment-Heisenberg-lift.md)原compatible moment/proper Heis/43格FL及全noncusp已付。§§17–19以Λ°=lim Rr[E[p^r]]/Rr[0]的真实norm根塔给连续all-vector矩，Mprim_d=(1−p^d)Mtilde_d。原两路径反差分支付同根ρ和完整中央二次gauge；S/U整恒等式适用全部标记，完成Gcorr之后H0/H1Z0给唯一兼容过渡，原n2/n5算术未平滑识别最高整子商。§20新增Λ°≅I及D=12的整jet J=I/I¹³≅⊕₁¹²Sym^dH，自由秩90；log/exp全GL2等变、原mom_d=d!pr_d，双槽保i!j!，逐层兼容。只有限化系数，未交换raw period/PD极限或改变Cartan I仅modp。

[R1148–53](results.md)原cusp/global基、relative Hodge/Frob、finiteFL尺度全沿open/逐字前态。Ccyc=exp(9^(224·9⁴))；大aux affine实际存在，不代空集。β3/β5及J=Har(1,3,4)给真障碍rs h−zab，七退化支、最高同源组合、U/U²尺度/β底参数全保；两β坏不外推η★=1，原F0/完整深盘继续。

[R1155 §§1–16](results/R1155-original-primitive-dilogarithmic-Frobenius-readout.md)原raw rational Bst/whole path、全部S3/五项/坏点N²/形式ψ已付，G=(logu,log1u,−Li2u)。真实LT g=z^(p²−1)−p的PD窗口只保r=i−w_b、j<p，系数(−1)^r/r!，全向量零iff所有selected normal系数0；43格/二次tensor界14/28。完整公式沿open/原文，R985高坐标carry未删；仍须同一原整frame的实际central gauge及F0。

[R1162](results/R1162-original-CM-function-blocks-and-PD-normal-coefficients.md)给真实e-block：m_jr=r!Σ_(k≥r)binom(k,r)p^(k−r)c_(j+ke)，所需精度k≤i、p^(i−k+1)；原FL窗口阶乘精确消，仍须同一整frame。

[R1156–60](results.md)原四线raw/SV全noncusp、GL2/rank1下降、crossed J_n及实际算术B_n已付；h0=(hV+B_n)/v_n，n2/n5覆盖p>37，全p^r三中心保λ∞。同根/27项/七行坏参数及来源沿open/逐字前态。一般Frob仍须实际b(q⁻¹T′q)，Cartan I仅modp、原F0未读。

[R1163 §§1–10](results/R1163-original-highest-moment-integral-syntomic-comparison.md)原系数的exact integral syntomic比较已覆盖完整43格：Tsuji2000小权+E^d signed整projector给Hq(q≤t)；三中心统一放E12/Sn14，pair antisym准确Π0/2/4无组合数。实际Poincaré类−c1(P)/2由∆*degree−2锁Weil coeval1，四份补原λ∞xγ5，全部weight14。原完整primitive groupoid及全塔兼容已识别，ordered所有交叉项/有限H0全保；继续theta/Miller同根代表至适配FL frame及normal表，未冒F0数值。

[R1164 §§1–13](results/R1164-original-pointed-Miller-coefficients-and-Cech-symbols.md)原first-Weil pointed线、inverse根/chord/全塔及整PD cocycle已付：−C(U_i)、−log_PD H_ij保μN相位，所有lift/加法/降层/ordered同伦沿原文。§13实际SS frames为a·t/tP、a，a=t(−P)；div_model f=N(P−O)−Nv_L(a)F，两个u真整unit，LT参数改变保c0及unit ratios。原scalar/closed Cor给Mtilde；继续refinement与Frob-overlap至原normal/F0，不在NP≠0时冒同一unit。

[R1165](results/R1165-original-integral-residue-contraction-and-log-PD-cone.md)原odd两开集DR有显式整收缩：ηV=η−t⁻²dt，π(αU,αV,h)=(Res(αU/t−hηV),Res(hω))；x^aω/yx^a单位首项消主部给dH+Hd=1−ιπ，filtered且p连续。tensor/原projectors后保底log方向，cone d0=(N,1−p⁻ʳΦ)、d1=(1−p^(1−r)Φ)−N。actual chain F时Q=πF_rH，第二槽须+Qα；不能只用Φ_M宣Q0。正常N双对角、c≡−1−γp、I_h精度商均付；继续实际Miller refinement/Frob-overlap和normal/F0。

## O1：原两 jet、Gauss–Padé 与固定 Dixon

[R1137](results/R1137-original-Lame-conjugation-with-complete-boundaries.md)原Padé双缺陷⇔P,Q含x²，约后degree≤N−2/contact2N−1；全部首余项/P_N单位、Pell W非零但W0未unit。[原Dixon](notes/2026-11-28-original-genus-four-Dixon-Jordan-chain.md)保全Hesse/Schur/Jordan，normal=12tr(adjQ A²)非spectral，指定中列未cyclic。R1145及旧窗口/Prym只消费。

[原genus4](notes/2026-11-28-original-genus-four-global-Raynaud-vanishing.md)原canonical P22、六123映射/p次补偿、V4三平移及A/B/W全源已付；顶U^p与b6不同源，全部相位沿open/原文，不能替指定两jet。

[quadric续篇 §§1–8](notes/2026-11-28-original-Fermat-six-quadric-Cartier-continuation.md)原A=D³I和全kernel给a3=2ρδK4/b0−4vα、α=−2ρe/(b0δ)，原P³有序槽及P²W已定标。高Lamé零模Z的全上下分裂给R0=g/U^(m+1)、K=UDR0、DK=1+v²R0/U，C R0=ρe/(vδ)，e0下C(Ψ³K)=−ρδK4。Z的unit不代任一半段。

§8新增**e=K4=0 iff D^(p−5)K=0**：M0=K²−v²R0²的全部高极相消，DM0=2K；C M0=−v²e/(δzN U′)，保真实第三类。e0 iff唯一有界M1，自动积分M2后C M2=ρK4/(3δ²)；K40 iff有界M3，自动M4，K=D⁵M4/2。全部极≤(m−1−j)(Q+−Q)，首2τ^(j+2)/(j+2)!；完整norm式保D⁶M4−2常数，首τ⁶/360不代无解。继续同一三极有理函数的二次限制，σ/Λ/T仍未unit。

## O2：原 Gaussian 全 good-mask 与共同纤维

[R1127](results/R1127-original-Gaussian-irregular-complement-and-affine-cuspidal-label.md) p4k3且p|Bp−3时χ2 coarse一次unit只付跨盘；盘内须高度，余支p∤Bp−3。[R1129](results/R1129-linear-many-nonconstant-original-Gaussian-profiles.md)线性多个非constant不代独立/注入。

[R1135 §§1–17](results/R1135-original-Gaussian-low-row-fiber-constraint.md)两实际twist已统一z∈Fp；good代数Fp[W²,W(W²−d)]或Fp[W]，仅d非零平方余对待排。原heat/Hasse/Katz、fixed minor、norm2/CM gauge及全尺度见open/归档，顶unit不代det，向量场闭性未付。

[R1154 §§1–17](results/R1154-original-Gaussian-first-profile-and-joint-finite-Gauss-moments.md)真实Legendre/finite-log/Jacobi全部weighted边界、四低jet和3/8 Bernoulli项均付。原ξ=P/(a²V)、forcing6a²、Hasse负号及自足Xp按open/原文；p1019仅否无条件旁零，不扩扫。端点unit不代原v−3a⁶bu，joint继续。

[R1161](results/R1161-original-Gaussian-all-row-Bol-Legendre-transport.md)现付**全部原实际行**到同一固定ν的真实运输。Bol Θ^m g_j=A∂g_m+(m/12)Bg_m（m=p+1−j），Wilson反射不除Bernoulli；j=2s、原η及N_R完整保留。令Q_s=G_(2s)(−1/48,−w/864)、κ²=−1/(12aν⁴aG)，原行差=N_R 2^sδ(2s−1)!/s!·R[P^(s−2)Q_s{(V+κηP)^s−(V+κη′P)^s}]。仅even幂存活，形成Fp[η²]的T_s；两twist及missing principal沿原source。s3精确回H_p，δβG=12ε_r aν²aG。全mask共同纤维等价所有实际T_s相等；不再把这个运输列为未付，仍须用真实Q_s权重排除非对角对，未宣mask闭合或joint非零。


## 已成、禁止重做与其它入口

[R1125](results/R1125-original-full47-rational-point-classification.md)原完整47Q恰八CM，全部4513 whole盘/高度/全维来源和后到q²审计已成，不重跑47/41/旧端值窗口；run/hash沿原文/归档。

同h仍须本原/Legendre/实际mask；full-span/全p稳定已否，特定A/E4/mark未否。原σ/cY、η_h、d/N、nonp/Poincaré/splitting不能删；R907 artifact真404不据摘要重造。O3–6沿open/归档；主标准未达，继续。
