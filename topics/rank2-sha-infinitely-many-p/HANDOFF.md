# 交接

## 主目标与执行规则

固定一条E/Q，完整证明rank≥2且无穷不同p的通常全Sha[p∞]有限。**未完成，持续研究；不因阶段结果、时长或等回复收尾。**
- 最近已读规则提交：0f74fb43a6eba2646e34b2950f5de1131470fe29；2026-11-16 08:55:42 UTC核两README无变。实际CI pull 2026-11-16 08:43:16 UTC/8c72a832e334d34e16c0a2ce41a9dfef578587b7（两README差异空）。本地末次成功2026-11-14 21:35:50/7aa38f25e；最近本地重试2026-11-16 08:55:41 UTC仍无环境。最迟2026-11-16 09:30 UTC再实际pull。
- 仅写Rogerhu12/math-research-public/main；旧库授权789d22af全文已读。每条完整结论即时推；拒推立即实际pull --rebase尝试并用新head非强推循环到成功。不改他人历史，不落盘/回显令牌。
- 根/题README blob为21bd547f56590b7f2dd279d0297efb289a9b2783、965ab236bbd6753acb812b45fcc36ae9b6f83b3c；root15@708f058a差异已读。每次实际pull核两README差异、仅读变更、记提交，至少每小时。
- 数学执行仅公开Actions；可重算输出不入库/Release、不分块，仅producer/args/run/hash。H<10KB，MD/API<100KB，open尽量<30KB，单文件<5MB，题≤200MB；题log每轮≤5行，不写根LOG。
- 库存32,251,727B/2377文件，无超限，3旧真实输入块；[规则15来源](notes/2026-11-15-recomputable-output-provenance.md)保已删206输出、79未匹配/2自读/3旧块。环境不可用；实际CI pull与API读head分清。

## 完整检查点与分工

[本次压缩前完整H](notes/2026-11-16-frontier-before-rational-hecke-lattice.md)、[完整旧结论索引](notes/2026-11-16-results-index-before-original-hom.md)和[完整open](notes/2026-11-16-open-before-low-hurwitz-and-map-execution.md)沿链保全部旧公式、来源、条件及未闭门。入口results.md、notes/PROOF-INDEX-R851-R900.md、open.md。R1–363、365–560、562–653、655–711、713–874已登记；R364/R561/R654/R712和主目标仍开。旧未推R235/R237已重做。
root唯一metadata/ref写者；deep算R828实际第二/第三页；theta算原C24交叉链与四B；literature算原实际Hom函数和交点。子问题完成即续open。

## 当前第一实际门：原Hom与原shadow

原Z的R804/806/811/814角色、全Euler/period/good pair、R831的Z02=Z/Z20=−Z及6/12/1632/816完整保前检。7993仅检测canonical，不能转给Zorig。R858付原三垂直χ零及generic单射，故原Z零 iff同Tτχ零，值未判。单λ/root−与full toric λ×λ♯/root+双零不互换。
[R859](results/R859-original-supersingular-shadow-and-integral-aj-detection.md)及附录保惯性r剩余域F_(r²)、φ²−r、原整shadow与倒置6r的Chow逆；5/11排H1 torsion。全部Artin、闭点迹、边界和交重下 S(ΠΦX)=Alb H_*(G−φF)^*O。某实际ℓ>3 shadow非零即付同原AJ/Z。
[完备性](notes/2026-11-16-original-cm-inert-shadow-chebotarev-completeness.md)付固定ℓ原AJ非零 iff某惯性shadow非零 iff阶无界，每阶门正密度；原非零和无穷系数p都未付。

R862/R864固定原17挠点乘积h、H9/L、全Λ((2))=−2、τ/ℓ/c与可逆三Hom矩阵；原cusp(1,1,4)/Schoen极6/三商后2不代非零。v=h³/2^32=−122465−47628a−314892a²/17，a³17，整数n未知，不认Manin1；R866附A现已付17|n的必要条件（非充分）。
[R864附A](results/R864-original-seventeen-torsion-exact-field-and-cocycle.md)：e=18−7a、η=e⁻¹=324+126a+49a²，η²=−av；v_sm=e³v=7−18a²/17有小三次式。整单位同构(X,Y)↦(e²X,e³Y)使微分ηHi、n/次数不变，(nη)³v_sm=n³v，不能假称降低搜索度数。

R866/R869原Cv:Y²+vY=X³，Ξ_i*ωv=Hi，Ai=2^11κΞi；H0/Ξ0真下降F=Q(∛17)。公开run43822409558固定全cocycle；run43825112263给T9/Φ17（18×18/总34/291项）及三H541项（各98非零/含2）；脚本/参数/hash齐，不保存重算输出。
[R870](results/R870-original-low-weight-quotient-and-exact-elliptic-coordinate-certificate.md)：D=X0(867)，h=H0³∈S6。A,B∈M_k，C=(DQ A)B−A DQ B，C³=n³hA²(A+vB)²B²检查0..612(k+1)并保原germ/∞即认nΞ0。k2维120/低409/末1836；成功degree≤204，真degree≤119保证k2解。低核任意非零元同一比值，可有共同cusp零。
**公开执行已付**：旧run43827859642的(1,2)/(2,2)完整410×240模矩阵均满秩，k4取消无结果；run43832115772已付17参数门。R873 run43832670630/job133181502585在3.862秒完成原全部CM范数：d0∈(81734.1176,81734.1177)，g∈(26753.0337,26753.0338)。全整unit实际degree>23194880，3同源>7731626，故k2/4/6/8全部排除，不再启动该轨道低权矩阵。脚本/参数/run/hash见R873。

[R867附A/B/C](results/R867-original-single-hom-and-integral-hecke-three-basis.md)：整R=2T7²+7T7−8T13−28与R²−2给两真unit、完整乘法表和整packet逆；全8/64/14邻点/Artin保。首系数不得免费归一，unit保持同n可积集合；认证后3n三基真整（旧57改进）。3同源备选Ψ=φΞ0/3成功经dual直接回nΞ0，但仅n0|nΨ|3n0，尚未付整性/度数改善。
**R874实际候选**：原全q必要格I∞=u*OE，u*=(915+1097θ+2962eps2)/55569，NormI17/55569；λθ=−497+237a−17a²、λeps2=609−44a−75a²。λu*=(68+7a−13a²)/3，u*(106+59θ+185eps2)=17。run43834068620/job133186195650在4.013秒PASS：全packetdegree>364.3945排k2；u*准度数距376<10^-88，未取整/未认Hom。root续k4/6真实坐标，以M2乘积构基避免旧M4慢构造；成功返回17Ξ0后恢复三Hom/原Artin和R859shadow。R875原17挠点有限E2/精确Gram producer已发布；literature完整证明中，未据整数准度数认Hom。

## 当前第二门：四原B的实际同源关系

原S34/T72/U136/V66、charge17/36/68/33、CM13、全Euler/p²p³保。R816/820付E−11 rank≥2，通常全Selmer桥仍缺同一无穷p完整J′非零。
R855/R856 whole整除p与全参数Frobenius、[半Bol](notes/2026-11-16-original-half-bol-and-cm-divided-residue.md)的两ε/V_N/留数p相消、共同A24的固定相对theta核全部保。
[共同C24](notes/2026-11-16-original-common-odd-degree24-and-three-row-pairing.md)：C24=−σ24x²yQ2/7、Ej=−b^jσ24x^(8−3j)y、c*=(1,−4/7,16/7)。四B零 iff BS0且M_pc*0；三相邻系数来自四不同真实伙伴，U二挠仍同全tensor/lift。S/V的X0/729X0真实低卷积、[3]完整W3及S/U六零不省略。
R860/R863保 Cp−cD^p=D·N²Q/(2mnM)、奇N项与全法向伙伴；r2含Ξ+σ2²L/4，r3含全部连接及σ2 Ltilde。边界27/7、首尾unit或Frob递推不代指定四B forcing。
R863附A付span(Zj)与原三算术线恰二维交、商坐标−4c0+c1+2c2；真实f2在剩余方向。唯一全纯C2满足Z2=∇C2−351/(2816b)Θ17，whole除p行保首对数商/所有低卷积，不能增中央零。theta续同M_pc*/BS。

## 当前第三门：低松弛同P/R/S的真正后两页

原M=c*U0w13J保P134/总charge40/39carry/10980/十九角/全WD，TM=s−r−13与TJ=s−r不混。
[R828四位](notes/2026-11-16-r828-actual-one-scalar-four-digit-and-same-correction-pages.md)、[三carry](notes/2026-11-16-r828-three-native-carry-recursions-and-last-block-tails.md)、[左行/Newton](notes/2026-11-16-r828-native-zero-angle-reader-and-central-newton-value.md)保hΘ=H w^(s−4)B全高尾、M四位、同P/R/S及Y1/p、Y2/p。首提升迫W0/W1 modws零及W2+H w^(s−4)BW3 modws零；新增D2/D3只读W3八/十二尾及末quartic，仍联立normal；ell=s−14保[w]W4。
Λ0M(X)/p=Σ_(d1..3)p^(d−1)a^-d[w^ds]Wtilde_(r^(d))(X)，r=(Q−40)(Q−41)(Q−42)，无1/d!。四中央零给Hc=h0−C/D、H−Hc∈p³，真实必要式N(P)+pN(R)+p²N(S)=0 modp³；其它三中央残差不删。
R861/R865实际a*=−34C_H对齐保持M，H/h0有限乘积与三谐和位给Rcal；真实g^flat含hΘ，quartic k13首像旧unit、k>13此行恒零，参考g0须恢复3H[w4]BW3。R865附A全证 L1=q2/3−3q3/4+1/3 modp；不假其非零。
R868原σ_t=min(ord P_n−A_n)控制t^-τ返回；τ=k−13≤σ_t且ell≤s−h时首像unit，故Λ0不下降第二页左行，R/S调标量同时改全余类。最小r=b0=3,c0≤2时σ_t0，仍开。
[R871](results/R871-original-sigma-thirteen-unit-and-low-hurwitz-readers.md)：真实V_S^-13单位保w13/39carry，BΦ=Φ/S13全whole并保P134/十九角；完整ΛS给D1/Dp+2/D2p+3、J0和绝对γ。模p行差仅39低带，整高尾不能删；k>13首位仍零。deep续低松弛同P/R/S与四原中央，不再新增gauge等价或免费伙伴。

- [R872及附A](results/R872-actual-quartic-third-carry-and-central-first-digit.md)：τ1/2/3第三carry对H首高位响应−6ab0γF（第二块+12a保），同X必要Bτ+6aγF Qc=0。更早同P+pR第二页baseline₂+a²b0γF/3=0，调整口为K1末三W2尾。τ4改用Λ0，响应−36b0γF/a²、第二页加2b0γF/a；τ≥5仅这39carry/Λ0看不见H首位。原未知baseline、全同R/S、normal及四中央不删。

## 其它原门与同步

R834/836单位块、R837三长/两长和自然47/12的q1/2缺口保；旧47/8须真第三长，HN为9κ−3χ−12b。R840同Kcorr/Hcorr两高前缀、第三3η/第四短行、末同cF³仍未全付；disc²读所有分支。R842 WT上[b0]=−BD−Pr未知，全部negative/moving/十九角/同P保。
O4/O6/O7、R364/R561/R654/R712及全部旧open未闭；有限p、复秩1、局部unit、条件height或别cycle不完成；AST/strict/fine不替通常全Selmer。
08:43:16实际CI pull成功，run43833512920/job133184339456/head8c72a832，两README差异空且blob一致；下一09:30前。R874修复后run43834068620成功，原候选已列；坐标仍未认证。
