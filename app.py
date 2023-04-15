import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import time
import plotly.express as px
import plotly.graph_objects as go
import figures as f
import icons as icons

st.set_page_config(page_title='Airdrops',  layout='wide', page_icon='images/airdrop.png')

proj_title = '<p style="font-family:sans-serif; color:white; font-size: 50px;"><b>Airdrop Notes</b></p>'
gap = '<span>&nbsp;&nbsp;</span>'

t1, t2 = st.columns((1,5))
t1.image('images/airdrop.png', width = 120)
t2.markdown(proj_title, unsafe_allow_html=True)
t2.markdown("""*Last Update: April 15th 2023*""")


#=========================== OVERVIEW ==============================
st.markdown(
    """
        # Overview 
        
        This page is designed for the purpose of internally tracking key airdrop information. 
        
        ### Combating [Sybil](https://medium.com/@Beosin_com/a-closer-look-at-the-anti-sybil-mechanism-under-the-arbitrum-airdrop-hype-5fd6405a2604) [detection](https://mirror.xyz/x-explore.eth/AFroG11e24I6S1oDvTitNdQSDh8lN5bz9VZAink8lZ4):
        1. Use Alchemy end points for MetaMask (Avoid IP Tracking; Free Alchemy account --> #app cap at 5)
        2. No interactions between wallets 
        3. Initial capital from CEX - **Different amt & dates!!!!**
        4. Need to change all wallets after cashing out (wallets are linked once sent to same CEX address)
        5. Differentiate behavior patterns -> dates and smart contract interactions
         
        More (in Chinese): https://www.youtube.com/watch?v=nv2YlCCubG8
""")



st.markdown(
    """

    ---
    # Airdrop Pros Activities
    
    Wallets that have received most of past significant airdrops (eg. ARB, OP, BLUR, SOS, LOOKS, ENS, DYDX, 1INCH, UNI, HOP, FORTH, GTC)
    
    1. [0x6f9bb7e454f5b3eb2310343f0e99269dc2bb8a1d](https://debank.com/profile/0x6f9bb7e454f5b3eb2310343f0e99269dc2bb8a1d)
    2. [0x11B1785D9Ac81480c03210e89F1508c8c115888E](https://debank.com/profile/0x11B1785D9Ac81480c03210e89F1508c8c115888E)
    3. [0x70e7a6621f4cb3c3e073d0539899f49fc88424c0](https://debank.com/profile/0x70e7a6621f4cb3c3e073d0539899f49fc88424c0)
    4. [0x78Ebe56BC138069557C89af35EB29023fF31Ae2c](https://debank.com/profile/0x78Ebe56BC138069557C89af35EB29023fF31Ae2c)
    5. [0x000f4432a40560bbff1b581a8b7aded8dab80026](https://debank.com/profile/0x000f4432a40560bbff1b581a8b7aded8dab80026)
    6. [0xd56EE5Ba5A52e15f309108BDd6247C69B4F624C2](https://debank.com/profile/0xd56EE5Ba5A52e15f309108BDd6247C69B4F624C2)
    
    Protocols/contracts the above wallets interacted with in 2023 that do not have tokens yet (as of last update date):
    - More than one wallet: 0VIX, Sync Swap, ZkSyn Era, Azuro
    - Only one wallet: LayerZero (other wallets potentially have done the interactions in 2022); Vela (beta closed); TBD
    
    Protocols/contracts the above wallets interacted with in 2022 that do not have tokens yet: TBD


    """
    , unsafe_allow_html=True
)

st.markdown(
    f"""
    ---
    # Potential L1 Airdrops
    
    Priorities: **:green[HIGH]**, **:blue[MEDIUM]**, **LOW**. Ignore Sui as the team confirmed no airdrop. 
    
    ### :green[LayerZero: TBD]
    
    1. Buy STG and stake. Vote.
    2. Bridge to aptos through Liquidswap
    3. Use Sushi Xswap (cheapest between Fantom and Poly)
    4. Use USDC bridge (testnet currently closed)
   
    ### Fuel: TBD 
    ### Zeta: TBD 
    ### Aleo: TBD 
    ### Shardeum: TBD 
    ### Celestia: TBD
    
    ### Sei: TBD 
    Testnet since 2022. and only 1% supply for airdrop?
    
    
    """
    , unsafe_allow_html=True
)

st.markdown(
    f"""
    ---
    # Potential L2 Airdrops
    
    Priorities: **:green[HIGH]**, **:blue[MEDIUM]**, **LOW**
    
    ### :green[ZkSync: High Chance] 
    
    Token launch around April 2024. *(need to confirm)*
    1. Cheapest bridge: using Orbiter (ETH: Poly to zkSync Era) (min 0.006ETH; more required for bridging to zkSync Lite)
    2. One time: provide liquidity on SyncSwap (2-3 u each time)
    3. Weekly / monthly: trade on SyncSwap, Velocore, Zigzag (zkSync Lite only), Nexon Finance. Ideally use everything once (to increase # of smart contracts used), then keep using SyncSwap (SYNC launch confirmed).
    4. Frequency TBD: mint zkSync NFT on 4everland (Step 2 in [link (in Chinese)](https://zhuanlan.zhihu.com/p/615574075)) 
    
    Step by step w/ screenshots (in Chinese): https://www.youtube.com/watch?v=e0vlQjQWATU
    The video covers step2&3 above. Step 1 in video uses SyncSwap. While such bridging is more expensive than Orbiter, it does increase the chance of 
    a SyncSwap airdrop.
    
    ### :blue[StarkNet]: TBD 
    
    Big project, but hard to use. Questionable token value after launch.
    
    ### :green[Mantle: Unconfirmed] 
    Mantle Core Proposed 200M Fund for Web3 Startups - 100 from BitDAO (Feb 2023)[{icons.info_icon}](https://cointelegraph.com/news/bitdao-s-mantle-core-proposes-200m-for-web3-fund)
    
    Currently on testnet only, thus free for interactions. Auto scripts available. [{icons.info_icon}](https://zhanghao.btc666.cc/)
    
    Testnet just recently launched --> higher priority compared to Scroll. 
    
    ### :blue[Scroll: Unconfirmed]
    Total funding 83mil; valuation at 1.8bil; new funding 50mil in 2023 [{icons.info_icon}](https://www.theblock.co/post/217340/ethereum-scaling-scroll-50-million-funding-round-1-8-billion-valuation)
    
    Currently on testnet only, thus free for interactions. Auto scripts available. [{icons.info_icon}](https://zhanghao.btc666.cc/)
    
    ### Aztec: TBD 
    
    ### ZkLink: Confirmed [{icons.info_icon}](https://zklinkdefi.medium.com/dunkerque-zklink-evacuation-plan-ea7e7dd7bef0)
    
    0 cost Testnet transactions. Wait till escape routes built by community members. Questionable community engagement.
   
        
    """
    , unsafe_allow_html=True
)

st.markdown(
    f"""
    ---
    # Potential Other Airdrops
    
    Priorities: **:green[HIGH]**, **:blue[MEDIUM]**, **LOW**
    
    ### :green[0VIX: Confirmed] [{icons.info_icon}](https://t.me/OVIXProtocol/1168)
    
    ### :blue[SyncSwap: Confirmed] [{icons.info_icon}](https://twitter.com/syncswap/status/1643750342776217601)
    
    See zkSync. However, to maximize the possibility of a SyncSwap airdrop, bridging using SyncSwap is necessary. 
    As SyncSwap currently only supports bridging from ETH mainnet to zkSync, it is more expensive than Orbiter for bridging (due to higher gas fee).
    
    ### :green[Azuro: Confirmed AZUR] [{icons.info_icon}](https://azuroprotocol.medium.com/azuro-is-now-on-polygon-and-the-azuro-score-is-live-b09fe409e67c)
    
    ### :blue[Bungee: Confirmed]
    
    """
    , unsafe_allow_html=True
)


st.markdown(
    """

    ---
    # Methodology 
    
    TBD.

    """
    , unsafe_allow_html=True
)

st.markdown(
    """
    
    ---
    # About
    
    This dashboard is designed by [@Phi_Deltalytics](https://twitter.com/phi_deltalytics). 
    Any comments and suggestions are welcomed. 
    
    """
    , unsafe_allow_html=True

    )












