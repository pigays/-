import streamlit as st
import time

st.set_page_config(page_title="피부 타입별 화장품 추천 시스템")

st.title(" 피부 타입별 화장품 추천 시스템")
st.write("청계중 영재학급 5조 산출물")
st.divider()
skin = None

# 닉네임 입력
name = st.text_input("닉네임을 입력해주세요 :")

if name:
    st.write(f"안녕하세요, {name}님 :)")
    st.write("저는 피부 타입에 맞는 화장품을 알려주는 시스템입니다!")
    st.info("🞷 [Tip] 아래 질문에 따라 선택지를 골라주세요!!")

    st.divider()
    know = st.radio("자신의 피부 타입을 알고 계신가요?", ["네" , "아니요"])


    if know == "아니요":
        st.write("피부 타입 확인을 위해 간단한 테스트를 시작하겠습니다!")

        q1 = st.radio("1. 세안 후 피부 속건조가 있다.", ["o" , "x"])
        q2 = st.radio("2. 피부가 얇고 건조하다.", ["o" , "x"])
        q3 = st.radio("3. 각질이 자주 생긴다.", ["o" , "x"])
        q4 = st.radio("4. 피부가 기름지고 번들거린다.", ["o" , "x"])
        q5 = st.radio("5. 블랙헤드나 화이트헤드가 많다.", ["o" , "x"])
        q6 = st.radio("6. 여드름이나 트러블이 자주 생긴다.", ["o" , "x"])
        q7 = st.radio("7. 화장품을 사용하면 피부가 자주 따갑다.", ["o" , "x"])
        q8 = st.radio("8. 피부에 순한 제품을 쓰지 않으면 트러블이 생긴다.", ["o" , "x"])
        q9 = st.radio("9. 얼굴의 T존만 번들거리고 양볼은 건조하다.", ["o" , "x"])

        if st.button("피부 타입 결과 보기"):
            if q9 == 'o':
                skin = '복합성'
            elif q7 == 'o' or q8 == 'o':
                skin = '민감성'
            elif (q2 == 'o' and q1 == 'o') or (q3 == 'o' and q4 == 'x' and q5 == 'x' and q6 == 'x'):
                skin = '건성'
            elif (q1 == 'x' and q2 == 'x' and q3 == 'x' and q4 == 'o'):
                skin = '지성'
            else:
                skin = '중성'
            st.session_state["skin"] = skin
            st.subheader(f"{name}님의 피부 타입은 {skin} 피부 입니다!")

    else:
        skin = st.selectbox("당신의 피부 타입은 무엇입니까?", ["지성", "건성", "복합성", "민감성", "중성"])
        st.session_state["skin"] = skin
        # 상태가 저장된 경우만 다음 단계로 이동
        if "skin" in st.session_state:
            skin = st.session_state["skin"]
            if st.button("화장품 추천 보기"):
                st.session_state["show_recommend"] = True
    
    if st.session_state.get("show_recommend", False):
        st.divider()
  if st.session_state.get("show_recommend", False):
        st.divider()
        if skin == "건성":
            st.write('건성 피부는 유/수분이 부족해서 얼굴이 자주 당기고 각질이')
            st.write('생기기 쉽다는 특징이 있습니다.')
            st.write('건성 피부는 피부에 충분하게 수분을 공급하는 것이 중요합니다.')
            st.write()
            st.write("건성 피부의 추천 화장품은 수분 크림, 히알루론산 토너, 보습 크림 입니다 :)")
            st.write("")
            if st.button("[건성] 구체적인 제품 예시 보기", key="dry_example"):
                st.session_state["show_dry"] = True  # ✅ 클릭 상태 저장

            if st.session_state.get("show_dry", False):  # ✅ 클릭 시 표시 유지
                st.divider()
                st.write("예시 제품:")
                st.write("1) 메디큐브 - PDRN 핑크 앰플 30ml 리필 기획")
                st.write("  올리브영 판매가 : 24200 원")
                st.write("  올리브영 평점 : 4.7점(16,315건)")
                st.write("")
                st.write("2) 이니스프리 - 히알루론산 그린티 씨드 수분크림 50ml")
                st.write("  올리브영 판매가 : 27000 원")
                st.write("  올리브영 평판 : 4.8점(741건)")
                st.info("⚠︎ 자극 가능성 있으므로 개인 피부 상태 확인 필요")
                st.info("⚠︎ 판매가는 행사에 따라 변경될 수 있음!")

        elif skin == "지성":
            st.write('지성 피부는 피부 번들거림이 잘 생긴다는 특징이 있습니다.')
            st.write('또한, 지성피부는 모공이 넓고 트러블이 발생하기 쉽습니다.')
            st.write('지성 피부는 꼼꼼한 세안과 유수분 밸런스를 맞추는 것이 중요합니다.')
            st.write()
            st.write("지성 피부의 추천 화장품은 수분 크림, 티트리 토너나 세럼, 나이아신아마이드 성분이 포함된 제품 입니다 :)")
            if st.button("[지성] 구체적인 제품 예시 보기", key="oily_example"):
                st.session_state["show_oily"] = True
            if st.session_state.get("show_oily", False):
                st.divider()
                st.write("예시 제품:")
                st.write("1) 라로슈포제 - 에빠끌라포밍 젤")
                st.write("  올리브영 판매가 : 31000 원")
                st.write("  올리브영 평점 : 4.8점(1099건)")
                st.write("")
                st.write("2) 이니스프리 - 히알루론산 그린티 씨드 수분크림 50ml")
                st.write("  올리브영 판매가 : 27000 원")
                st.write("  올리브영 평판 : 4.8점(741건)")
                st.info("⚠︎ 자극 가능성 있으므로 개인 피부 상태 확인 필요")
                st.info("⚠︎ 판매가는 행사에 따라 변경될 수 있음!")

        elif skin == "복합성":
            st.write('복합성 피부는 건성과 지성을 합친 타입 입니다.')
            st.write('피지 분비가 불균형하고, 부분적으로 모공이 넓어진다는 특징이 있습니다.')
            st.write('복합성 피부는 유수분 밸런스를 맞추는 것이 중요합니다.')
            st.write()
            st.write("복합성 피부의 추천 화장품은 수분크림, 피부 진정 세럼, 약산성 폼클렌저 입니다 :)")
            if st.button("[복합성] 구체적인 제품 예시 보기", key="mix_example"):
                st.session_state["show_mix"] = True
            if st.session_state.get("show_mix", False):
                st.divider()
                st.write("예시 제품:")
                st.write("1) 이니스프리 - 히알루론산 그린티 씨드 수분크림 50ml")
                st.write("  올리브영 판매가 : 27000 원")
                st.write("  올리브영 평판 : 4.8점(4522건)")
                st.write("")
                st.write("2) 제로이드 수딩 크림 80ml 기획")
                st.write("  올리브영 판매가 : 38,000 원")
                st.write("  올리브영 평판 : 4.8점(741건)")
                st.info("⚠︎ 자극 가능성 있으므로 개인 피부 상태 확인 필요")
                st.info("⚠︎ 판매가는 행사에 따라 변경될 수 있음!")

        elif skin == "민감성":
            st.write('민감성 피부는 외부 자극에 민감하게 반응해 쉽게 붉어지거나 따가움을 느끼며, 자극이 적은 제품을 사용해야 합니다.')
            st.write()
            st.write('민감성 피부의 추천 화장품은 저자극 제품, 알로에 수분 크림, 병풀추출물 성분이 들어간 제품 입니다 :)')
            if st.button("[민감성] 구체적인 제품 예시 보기", key="sensitive_example"):
                st.session_state["show_sensitive"] = True
            if st.session_state.get("show_sensitive", False):
                st.divider()
                st.write("예시 제품:")
                st.write("1) 웰라쥬 - 리얼 히알루로닉 블루 100 앰플 75ml 더블 기획")
                st.write("  올리브영 판매가 : 50,000 원")
                st.write("  올리브영 평판 : 4.9점(2,596건)")
                st.write("")
                st.write("2) 제로이드 수딩 크림 80ml 기획")
                st.write("  올리브영 판매가 : 38,000 원")
                st.write("  올리브영 평판 : 4.8점(4522건)")
                st.info("⚠︎ 자극 가능성 있으므로 개인 피부 상태 확인 필요")
                st.info("⚠︎ 판매가는 행사에 따라 변경될 수 있음!")

        elif skin == "중성":
            st.write("중성 피부는 유수분 밸런스가 잘 맞아 트러블이 적습니다.")
            st.write("그래서 피부에 특별한 관리가 필요하지 않은 타입입니다.")
            st.write("중성 피부의 추천 화장품은 수분크림, 약산성 폼클렌저 입니다 :)")
            st.write("")
            st.write("중성 피부는 특별하게 추천하는 제품명이 따로 없습니다!")
            st.write("화장품을 구매할 때 피부에 너무 자극적인 화장품 사용은 자제해 주세요!")

        st.info("⚠︎ 사용 결과는 저장되지 않습니다.")
        st.caption("청계중 영재학급 5조 산출물")
